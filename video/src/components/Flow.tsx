import { AbsoluteFill, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { accents, colors, fontFamily, ink, onAccent, safe } from "../theme";
import type { Word } from "../types";

// Bölümü birbirine bağlayan sahneler: açılıştaki "bu hafta" listesi (sondaki haber kilitli),
// kapanıştan önceki yorum sorusu ve takip çağrısı.

const Lock: React.FC<{ size: number; color: string }> = ({ size, color }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2.4} strokeLinecap="round">
    <rect x="4" y="11" width="16" height="10" rx="2.5" fill={color} fillOpacity={0.15} />
    <path d="M8 11V8a4 4 0 0 1 8 0v3" />
  </svg>
);

// Teaser: haberler numaralı satırlar halinde kayarak gelir; son haberin başlığı bulanık ve kilitli
// ("sona sakladık") — izleyicide sona kadar kalma merakı.
export const Agenda: React.FC<{ headlines: string[]; durationInFrames: number }> = ({ headlines, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const out = interpolate(frame, [durationInFrames - 8, durationInFrames], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const title = spring({ frame, fps, config: { damping: 14 } });
  const lastAt = 6 + (headlines.length - 1) * 7;
  const unlockPulse = 1 + 0.04 * Math.sin(Math.max(0, frame - lastAt - 10) / 4);
  return (
    <AbsoluteFill style={{ fontFamily, padding: `0 ${safe.side}px`, paddingTop: 330, opacity: out }}>
      <div
        style={{
          fontSize: 44,
          fontWeight: 700,
          letterSpacing: 4,
          color: colors.text,
          background: colors.yellow,
          border: ink.border(5),
          boxShadow: ink.shadow(8),
          borderRadius: 12,
          padding: "6px 22px",
          alignSelf: "flex-start",
          opacity: title,
          transform: `translateY(${(1 - title) * 30}px) rotate(-3deg)`,
          marginBottom: 44,
        }}
      >
        BU HAFTA {headlines.length} HABER
      </div>
      {headlines.map((h, i) => {
        const last = i === headlines.length - 1;
        const s = spring({ frame: frame - 6 - i * 7, fps, config: { damping: 15, mass: 0.6 } });
        const accent = accents[i % 4];
        return (
          <div
            key={i}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 28,
              marginBottom: 26,
              padding: "26px 30px",
              borderRadius: 28,
              background: last ? "#FFF3C4" : colors.card,
              border: ink.border(5),
              boxShadow: ink.shadow(10),
              opacity: s,
              transform: `translateX(${(1 - s) * 260}px) scale(${last ? unlockPulse : 1})`,
              transformOrigin: "left center",
            }}
          >
            <div
              style={{
                minWidth: 92,
                height: 92,
                borderRadius: 22,
                background: accent,
                color: onAccent(accent),
                border: ink.border(4),
                fontSize: 50,
                fontWeight: 700,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              {String(i + 1).padStart(2, "0")}
            </div>
            {last ? (
              <div style={{ position: "relative", flex: 1 }}>
                <div style={{ fontSize: 48, fontWeight: 700, color: colors.text, filter: "blur(16px)", lineHeight: 1.1 }}>{h}</div>
                <div
                  style={{
                    position: "absolute",
                    inset: 0,
                    display: "flex",
                    alignItems: "center",
                    gap: 16,
                    fontSize: 44,
                    fontWeight: 700,
                    color: colors.text,
                    letterSpacing: 2,
                  }}
                >
                  <Lock size={52} color={colors.text} /> SONA SAKLADIK
                </div>
              </div>
            ) : (
              <div style={{ flex: 1, fontSize: 48, fontWeight: 700, color: colors.text, lineHeight: 1.1 }}>{h}</div>
            )}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};

// Yorum sorusu: konuşma balonu içinde kelimeler seslendirildikçe belirir, altta "yorumlara yaz" oku.
export const QuestionCTA: React.FC<{ text: string; words: Word[]; startS: number }> = ({ text, words: timed, startS }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const words = text.split(" ");
  const pop = spring({ frame, fps, config: { damping: 11, mass: 0.6 } });
  const at = (i: number) => (timed[i] ? Math.round((timed[i].start - startS) * fps) : i * 4);
  const nudge = Math.sin(frame / 4) * 14;
  return (
    <AbsoluteFill style={{ fontFamily, justifyContent: "center", padding: `0 ${safe.side}px`, paddingBottom: 260 }}>
      <div
        style={{
          position: "relative",
          background: colors.card,
          color: colors.text,
          border: ink.border(7),
          borderRadius: 56,
          padding: "70px 60px",
          transform: `scale(${pop}) rotate(${(1 - pop) * -6}deg)`,
          transformOrigin: "left bottom",
          boxShadow: ink.shadow(16, colors.yellow),
        }}
      >
        <div style={{ fontSize: 34, fontWeight: 700, letterSpacing: 5, color: colors.blue, marginBottom: 22 }}>SANA SORUMUZ</div>
        <div style={{ fontSize: 86, fontWeight: 700, lineHeight: 1.08, letterSpacing: -2 }}>
          {words.map((w, i) => {
            const s = spring({ frame: frame - at(i) + 2, fps, config: { damping: 13, mass: 0.45 } });
            return (
              <span key={i} style={{ display: "inline-block", marginRight: 22, opacity: Math.max(0.12, s), transform: `translateY(${(1 - s) * 24}px)` }}>
                {w}
              </span>
            );
          })}
        </div>
        {/* balon kuyruğu */}
        <div
          style={{
            position: "absolute",
            left: 90,
            bottom: -44,
            width: 0,
            height: 0,
            borderLeft: "30px solid transparent",
            borderRight: "30px solid transparent",
            borderTop: `48px solid ${colors.text}`, // kuyruk: çerçeveyle aynı mürekkep rengi
          }}
        />
      </div>
      <div
        style={{
          marginTop: 110,
          alignSelf: "flex-end",
          display: "flex",
          alignItems: "center",
          gap: 20,
          fontSize: 52,
          fontWeight: 700,
          color: colors.text,
          background: colors.yellow,
          border: ink.border(5),
          boxShadow: ink.shadow(8),
          borderRadius: 14,
          padding: "6px 24px",
          opacity: interpolate(frame, [10, 20], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
          transform: `translateX(${nudge}px)`,
        }}
      >
        Yorumlara yaz
        <svg width={70} height={70} viewBox="0 0 24 24" fill="none" stroke={colors.text} strokeWidth={3} strokeLinecap="round" strokeLinejoin="round">
          <path d="M4 12h15M13 5l7 7-7 7" />
        </svg>
      </div>
    </AbsoluteFill>
  );
};

// Kapanış: logo, kapanış cümlesi ve "Takip et" butonuna dokunuş animasyonu.
export const FollowOutro: React.FC<{ text: string; logo: string | null; handle: string }> = ({ text, logo, handle }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const inS = spring({ frame, fps, config: { damping: 14 } });
  const tapAt = Math.round(fps * 1.1);
  const tapped = frame >= tapAt;
  const ripple = interpolate(frame - tapAt, [0, 14], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const press = tapped ? 1 - 0.08 * Math.exp(-(frame - tapAt) / 3) : 1;
  const finger = interpolate(frame, [tapAt - 14, tapAt], [140, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", fontFamily, color: colors.text, paddingBottom: 220 }}>
      <div style={{ opacity: inS, transform: `translateY(${(1 - inS) * 60}px)`, display: "flex", flexDirection: "column", alignItems: "center" }}>
        {logo ? (
          <Img src={staticFile(logo)} style={{ width: 620 }} />
        ) : (
          <div style={{ fontSize: 120, fontWeight: 700 }}>
            <span style={{ color: colors.blue }}>G</span>
            <span style={{ color: colors.red }}>D</span>
            <span style={{ color: colors.yellow }}>G</span>
          </div>
        )}
        <div style={{ fontSize: 50, fontWeight: 700, marginTop: 56, textAlign: "center", padding: "0 80px", lineHeight: 1.15 }}>{text}</div>
      </div>
      <div style={{ position: "relative", marginTop: 64 }}>
        <div
          style={{
            fontSize: 48,
            fontWeight: 700,
            padding: "26px 74px",
            borderRadius: 999,
            background: tapped ? colors.card : colors.blue,
            border: ink.border(5),
            boxShadow: ink.shadow(tapped ? 4 : 10),
            color: tapped ? colors.text : "#FFFFFF",
            transform: `scale(${press * inS})`,
            display: "flex",
            alignItems: "center",
            gap: 16,
          }}
        >
          {tapped ? (
            <>
              <svg width={44} height={44} viewBox="0 0 24 24" fill="none" stroke={colors.green} strokeWidth={3.2} strokeLinecap="round" strokeLinejoin="round">
                <path d="M5 12.5l4.5 4.5L19 7.5" />
              </svg>
              Takip ediliyor
            </>
          ) : (
            "Takip et"
          )}
        </div>
        {/* dokunuş: parmak izi daire + dalga */}
        <div
          style={{
            position: "absolute",
            left: "70%",
            top: "60%",
            width: 70,
            height: 70,
            marginLeft: -35,
            marginTop: -35,
            borderRadius: "50%",
            background: "rgba(17,17,17,0.55)",
            opacity: frame > tapAt + 16 ? 0 : interpolate(frame, [tapAt - 14, tapAt - 8], [0, 0.9], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
            transform: `translate(${finger * 0.6}px, ${finger}px)`,
          }}
        />
        <div
          style={{
            position: "absolute",
            left: "70%",
            top: "60%",
            width: 220,
            height: 220,
            marginLeft: -110,
            marginTop: -110,
            borderRadius: "50%",
            border: "5px solid rgba(17,17,17,0.6)",
            opacity: tapped ? 1 - ripple : 0,
            transform: `scale(${0.3 + ripple})`,
          }}
        />
      </div>
      {handle ? <div style={{ fontSize: 40, marginTop: 30, color: colors.muted, fontWeight: 500 }}>{handle}</div> : null}
      <div style={{ fontSize: 38, marginTop: 34, color: colors.text, fontWeight: 700, background: `linear-gradient(transparent 55%, ${colors.green}88 55%)`, padding: "0 8px" }}>Etkinlikler ve kayıt linki bio'da</div>
    </AbsoluteFill>
  );
};
