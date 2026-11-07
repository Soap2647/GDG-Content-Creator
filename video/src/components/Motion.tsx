import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { accents, colors, fontFamily, ink, onAccent, safe } from "../theme";
import type { Unit, Word } from "../types";
import { TopicIcon } from "./Icons";

// ---------------------------------------------------------------------------------------------
// Anahtar kelime: rakam/yüzde içeren ya da cümle başı olmayan büyük harfli kelime (marka, ürün, kurum).
// Kinetik altyazıda renklenir, kamera bu kelimelerde hafifçe "vurur".
export function isKeyword(w: Word, prev: Word | undefined): boolean {
  const t = w.text.replace(/[.,!?;:"“”()]/g, "");
  if (/\d|%/.test(t)) return true;
  const sentenceStart = !prev || /[.!?]$/.test(prev.text);
  return !sentenceStart && /^[A-ZÇĞİÖŞÜ]/.test(t) && t.length > 1;
}

// ---------------------------------------------------------------------------------------------
// Anahtar kelime kartları: anlatımdaki önemli kelime (önce rakamlar) ekrana tam genişlikte "çarpar".
// Ekranda en geç ~2.6 sn'de bir değişim olsun diye; aynı ekran görüntüsü 10+ sn durağan kalmasın.
export type Punch = { t: number; text: string; sub: string; segment: number };

const STOP = ["gibi", "ile", "ve", "veya", "kadar", "arasında", "dahil", "olan", "için"];
// Yalnızca baştaki/sondaki noktalama atılır: "1.2" ve "17.30" içindeki nokta kalmalı ("12", "1730" olmasın)
const core = (s: string) => s.split(/['’]/)[0].replace(/^[("“]+|[.,!?;:"”)]+$/g, "");

export function punchMoments(units: Unit[], skipValues: Record<number, string[]>, minGap = 2.6): Punch[] {
  const out: Punch[] = [];
  for (const u of units.filter((x) => x.kind === "narration" && x.segment)) {
    const cands = u.words
      .map((w, i) => ({ w, i, kw: isKeyword(w, u.words[i - 1]), num: /\d/.test(w.text) }))
      .filter((c) => c.kw && c.w.start > u.start + 1.0 && c.w.start < u.end - 0.6 && core(c.w.text).length > 1)
      .filter((c) => !(skipValues[u.segment!] ?? []).includes(core(c.w.text)));
    let last = u.start;
    // Rakamlar her zaman öncelikli; araya yer kalırsa diğer anahtar kelimeler (marka, kurum)
    const chosen = [...cands.filter((c) => c.num), ...cands.filter((c) => !c.num)]
      .reduce<typeof cands>((acc, c) => (acc.every((a) => Math.abs(a.w.start - c.w.start) >= minGap) ? [...acc, c] : acc), [])
      .sort((a, b) => a.w.start - b.w.start);
    for (const c of chosen) {
      if (c.w.start - last < 1.2) continue;
      // Rakamın yanına birimi yazılır ("430 sisteme"); bağlaç gelirse ("1071 ve") alt satır olmaz
      const next = u.words[c.i + 1] ? core(u.words[c.i + 1].text) : "";
      const sub = c.num && next.length > 3 && !STOP.includes(next.toLocaleLowerCase("tr")) ? next : "";
      out.push({ t: c.w.start, text: core(c.w.text), sub, segment: u.segment! });
      last = c.w.start;
    }
  }
  return out;
}

export const KeywordPunch: React.FC<{ text: string; sub: string; accent: string; durationInFrames: number }> = ({ text, sub, accent, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame, fps, config: { damping: 10, mass: 0.45 } });
  const out = interpolate(frame, [durationInFrames - 5, durationInFrames], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const size = text.length > 10 ? 120 : 168;
  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", paddingBottom: 260, opacity: out }}>
      <AbsoluteFill style={{ background: "rgba(243,238,228,0.9)", opacity: Math.min(1, s * 1.4) }} />
      <div style={{ fontFamily, textAlign: "center", transform: `scale(${0.4 + 0.6 * s}) rotate(${-4 * s}deg)` }}>
        <div
          style={{
            display: "inline-block",
            fontSize: size,
            fontWeight: 700,
            letterSpacing: -4,
            lineHeight: 1,
            padding: "18px 40px 26px",
            borderRadius: 26,
            background: accent,
            color: onAccent(accent),
            border: ink.border(7),
            boxShadow: ink.shadow(16),
          }}
        >
          {text}
        </div>
        {sub ? (
          <div style={{ display: "inline-block", fontSize: 64, fontWeight: 700, color: colors.bg, background: colors.text, padding: "2px 22px", marginTop: 30, transform: "rotate(2deg)" }}>
            {sub}
          </div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

export function keywordTimes(units: Unit[]): number[] {
  return units.flatMap((u) => u.words.filter((w, i) => isKeyword(w, u.words[i - 1])).map((w) => w.start));
}

// ---------------------------------------------------------------------------------------------
// Arka plan: krem kâğıt zemin, üst köşeden çok hafif segment rengi, kâğıt dokusu (gren). Parlayan renk lekeleri,
// neon ızgara ve koyu zemin "şablon/AI" görüntüsü verdiği için kaldırıldı (2026-11-07 editoryal tema).
const GRAIN =
  "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'>" +
  "<feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter>" +
  "<rect width='100%' height='100%' filter='url(%23n)' opacity='0.55'/></svg>\")";

export const Grain: React.FC = () => {
  const frame = useCurrentFrame();
  // Gren her 2 karede rastgele kayar (durağan doku "filtre" gibi durur)
  const k = Math.floor(frame / 2);
  const x = (Math.sin(k * 12.9898) * 43758.5453) % 300;
  const y = (Math.sin(k * 78.233) * 12345.6789) % 300;
  return <AbsoluteFill style={{ backgroundImage: GRAIN, backgroundPosition: `${x}px ${y}px`, opacity: 0.22, mixBlendMode: "multiply" }} />;
};

export const MotionBackground: React.FC<{ accent: string }> = ({ accent }) => {
  const frame = useCurrentFrame();
  const drift = Math.sin(frame / 140) * 4;
  return (
    <AbsoluteFill style={{ background: colors.bg, overflow: "hidden" }}>
      <AbsoluteFill style={{ background: `radial-gradient(120% 50% at ${15 + drift}% 0%, ${accent}1c, transparent 60%)` }} />
      <AbsoluteFill style={{ background: "radial-gradient(ellipse at center, transparent 60%, rgba(60,40,10,0.10) 100%)" }} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------------------------
// Kamera: yavaş itme + anahtar kelimelerde kısa "punch" (ölçek darbesi) ve hafif eğim.
export const Camera: React.FC<{ hits: number[]; children: React.ReactNode }> = ({ hits, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const last = hits.filter((h) => h <= t).pop();
  const dt = last === undefined ? 99 : t - last;
  const punch = 0.035 * Math.exp(-dt * 7);
  const push = 1 + 0.02 * Math.sin(frame / 120);
  return (
    <AbsoluteFill style={{ transform: `scale(${push + punch}) rotate(${punch * 12}deg)` }}>{children}</AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------------------------
// Haber geçişi: dört Google rengi şerit ekranı süpürür, büyük haber numarası ve başlık kelime kelime gelir.
// Köprü cümlesi (bridge) varsa numaranın üstünde küçük bir giriş satırı olarak görünür; son haberde "sona sakladık" etiketi.
export const SegmentIntro: React.FC<{ index: number; total: number; headline: string; kicker?: string; icon?: string; durationInFrames: number }> = ({
  index,
  total,
  headline,
  kicker,
  icon,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const accent = accents[(index - 1) % 4];
  const words = headline.split(" ");
  const final = index === total && total > 1;
  const out = interpolate(frame, [durationInFrames - fps * 0.35, durationInFrames], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const k = spring({ frame: frame - 8, fps, config: { damping: 14 } });
  return (
    <AbsoluteFill style={{ fontFamily, opacity: 1 - out }}>
      {accents.map((c, i) => {
        const p = interpolate(frame, [i * 2, i * 2 + 9, i * 2 + 14, i * 2 + 22], [-1.2, 0, 0, 1.2], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });
        return (
          <div
            key={c}
            style={{
              position: "absolute",
              top: `${i * 25}%`,
              height: "25.5%",
              left: 0,
              width: "100%",
              background: c,
              transform: `translateX(${p * width}px) skewX(-12deg)`,
            }}
          />
        );
      })}
      {/* Konu ikonu: numaranın sağ üstünde çizilerek belirir */}
      <div style={{ position: "absolute", top: safe.top + 230, right: safe.side + 10, opacity: interpolate(frame, [10, 16], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) }}>
        <TopicIcon name={icon} size={250} color={accent} delay={10} stroke={1.5} />
      </div>
      <AbsoluteFill style={{ justifyContent: "center", padding: `0 ${safe.side}px`, paddingBottom: 300 }}>
        {final ? (
          <div
            style={{
              alignSelf: "flex-start",
              fontSize: 36,
              fontWeight: 700,
              letterSpacing: 4,
              color: colors.text,
              background: colors.yellow,
              border: ink.border(5),
              boxShadow: ink.shadow(8),
              borderRadius: 12,
              padding: "8px 20px",
              marginBottom: 20,
              opacity: k,
              transform: `scale(${0.6 + 0.4 * k})`,
              transformOrigin: "left center",
            }}
          >
            SONA SAKLADIĞIMIZ HABER
          </div>
        ) : null}
        {kicker ? (
          <div style={{ fontSize: 50, fontWeight: 500, fontStyle: "italic", color: colors.text, opacity: 0.9 * k, marginBottom: 6, maxWidth: "70%", transform: `translateX(${(1 - k) * -40}px)` }}>
            {kicker}
          </div>
        ) : null}
        <div
          style={{
            fontSize: 300,
            fontWeight: 700,
            color: accent,
            lineHeight: 0.9,
            letterSpacing: -12,
            WebkitTextStroke: `6px ${colors.text}`,
            textShadow: `12px 12px 0 ${colors.text}`,
            opacity: interpolate(frame, [10, 16], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
            transform: `translateY(${interpolate(spring({ frame: frame - 10, fps, config: { damping: 12 } }), [0, 1], [120, 0])}px)`,
          }}
        >
          {String(index).padStart(2, "0")}
          <span style={{ fontSize: 80, color: colors.muted, letterSpacing: 0 }}> /{String(total).padStart(2, "0")}</span>
        </div>
        <div style={{ fontSize: 92, fontWeight: 700, color: colors.text, lineHeight: 1.05, letterSpacing: -2, marginTop: 24 }}>
          {words.map((w, i) => {
            const s = spring({ frame: frame - 14 - i * 2, fps, config: { damping: 14, mass: 0.5 } });
            return (
              <span key={i} style={{ display: "inline-block", marginRight: 22, opacity: s, transform: `translateY(${(1 - s) * 50}px)` }}>
                {w}
              </span>
            );
          })}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// Geçişten sonra başlık üstte küçük bir şerit olarak kalır (izleyici hangi haberde olduğunu bilir)
export const HeadlineChip: React.FC<{ index: number; headline: string }> = ({ index, headline }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame, fps, config: { damping: 16 } });
  const accent = accents[(index - 1) % 4];
  return (
    <div
      style={{
        position: "absolute",
        top: safe.top + 150,
        left: safe.side,
        right: safe.side,
        fontFamily,
        display: "flex",
        alignItems: "center",
        gap: 18,
        opacity: s,
        transform: `translateX(${(1 - s) * -60}px)`,
      }}
    >
      <div style={{ background: accent, color: onAccent(accent), border: ink.border(3), boxShadow: ink.shadow(4), fontWeight: 700, fontSize: 30, borderRadius: 10, padding: "2px 12px" }}>
        {String(index).padStart(2, "0")}
      </div>
      <div style={{ fontSize: 38, fontWeight: 700, color: colors.text, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>
        {headline}
      </div>
    </div>
  );
};

// ---------------------------------------------------------------------------------------------
// Kinetik altyazı: kelimeler konuşuldukça yaylanarak gelir; anahtar kelimeler renkli, aktif kelime vurgulu.
const MAX_CHARS = 22;

function chunk(words: Word[]): { words: Word[]; offset: number }[] {
  const out: { words: Word[]; offset: number }[] = [];
  let cur: Word[] = [];
  let len = 0;
  let offset = 0;
  words.forEach((w, i) => {
    if (cur.length && (len + w.text.length > MAX_CHARS || /[.!?,]$/.test(cur[cur.length - 1].text))) {
      out.push({ words: cur, offset });
      offset = i;
      cur = [];
      len = 0;
    }
    cur.push(w);
    len += w.text.length + 1;
  });
  if (cur.length) out.push({ words: cur, offset });
  return out;
}

export const KineticCaptions: React.FC<{ units: Unit[]; accentFor: (u: Unit) => string }> = ({ units, accentFor }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  // Kanca, köprü, soru ve kapanış kendi sahnelerinde büyük yazıyla zaten görünür
  const unit = units.find((u) => !["hook", "bridge", "question", "outro"].includes(u.kind) && t >= u.start - 0.05 && t <= u.end + 0.3);
  if (!unit) return null;
  const accent = accentFor(unit);
  const groups = chunk(unit.words);
  const group = groups.find((g) => t < g.words[g.words.length - 1].end + 0.12) ?? groups[groups.length - 1];
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: safe.bottom - 20, paddingLeft: safe.side, paddingRight: safe.side }}>
      <div style={{ fontFamily, fontWeight: 700, fontSize: 78, lineHeight: 1.18, textAlign: "center", color: colors.text }}>
        {group.words.map((w, i) => {
          const idx = group.offset + i;
          const kw = isKeyword(w, unit.words[idx - 1]);
          const appear = spring({ frame: frame - Math.round(w.start * fps) + 3, fps, config: { damping: 13, mass: 0.45 } });
          const active = t >= w.start && t < w.end + 0.08;
          return (
            <span
              key={i}
              style={{
                display: "inline-block",
                margin: "0 14px",
                opacity: Math.max(0.25, appear),
                transform: `translateY(${(1 - appear) * 30}px) scale(${active ? 1.06 : 1})`,
                transformOrigin: "center bottom",
                color: colors.text,
                // anahtar kelime: fosforlu kalem altı çizgisi (editoryal), parlama yok
                background: kw ? `linear-gradient(transparent 58%, ${accent}${accent === colors.yellow ? "" : "99"} 58%)` : "none",
                padding: "0 6px",
              }}
            >
              {w.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
