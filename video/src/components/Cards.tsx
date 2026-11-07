import { Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { accents, colors, fontFamily, ink, onAccent } from "../theme";
import type { Visual } from "../types";
import { Number3D } from "./ThreeD";

const cardStyle: React.CSSProperties = {
  background: colors.card,
  border: ink.border(5),
  borderRadius: 28,
  padding: 56,
  fontFamily,
  color: colors.text,
  width: "100%",
  boxShadow: ink.shadow(14),
};

// Kart girişi: alttan yaylanarak gelir, hafif dönüşle düzleşir
function useEnter(delay = 0) {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - delay, fps, config: { damping: 14 } });
  return {
    opacity: Math.min(1, s * 1.4),
    transform: `perspective(1600px) translateY(${(1 - s) * 140}px) rotateX(${(1 - s) * 18}deg) scale(${0.92 + 0.08 * s})`,
  };
}

// Büyük rakam: parlak 3D sayı dönerek yerine oturur (yalnızca kaynakta geçen, doğrulanmış sayı); birim ve açıklama
// altında çıkartma etiketi olarak. 3D font yalnızca ASCII içerdiği için Türkçe ön/son ekler 2D yazılır.
export const StatCounter: React.FC<{ v: Visual; index: number }> = ({ v, index }) => {
  const { width } = useVideoConfig();
  const target = v.stat_value ?? 0;
  const accent = accents[(index - 1) % accents.length];
  const ascii = (t: string) => /^[ -~]*$/.test(t);
  const prefix = v.stat_prefix ?? "";
  const suffix = (v.stat_suffix ?? "").trim();
  const num = `${ascii(prefix) ? prefix : ""}${target.toLocaleString("tr-TR")}${suffix && ascii(suffix) && suffix.length <= 2 ? suffix : ""}`;
  const unit = [ascii(prefix) ? "" : prefix, suffix && !(ascii(suffix) && suffix.length <= 2) ? suffix : ""].join(" ").trim();
  const enter = useEnter(10);
  return (
    <div style={{ width: "100%", textAlign: "center", fontFamily, color: colors.text, display: "flex", flexDirection: "column", alignItems: "center" }}>
      <div style={{ width: width - 2 * 72, height: 560 }}>
        <Number3D text={num} color={accent} width={width - 2 * 72} height={560} />
      </div>
      {unit ? (
        <div style={{ ...enter, display: "inline-block", width: "auto", fontSize: 72, fontWeight: 700, background: accent, color: onAccent(accent), border: ink.border(6), boxShadow: ink.shadow(10), borderRadius: 16, padding: "2px 28px", marginTop: -30 }}>
          {unit}
        </div>
      ) : null}
      <div style={{ fontSize: 54, fontWeight: 700, marginTop: 34, ...useEnter(16) }}>{v.stat_label}</div>
    </div>
  );
};

// Veriden çizilen bar grafik
export const MiniChart: React.FC<{ v: Visual }> = ({ v }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const labels = v.chart_labels ?? [];
  const values = v.chart_values ?? [];
  const max = Math.max(...values, 1);
  return (
    <div style={{ ...cardStyle, ...useEnter() }}>
      <div style={{ fontSize: 48, fontWeight: 700, marginBottom: 40 }}>{v.chart_title}</div>
      {values.map((val, i) => {
        const grow = spring({ frame: frame - 8 - i * 6, fps, config: { damping: 16 } });
        return (
          <div key={i} style={{ marginBottom: 32 }}>
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 38, marginBottom: 12 }}>
              <span>{labels[i]}</span>
              <span style={{ fontWeight: 700 }}>
                {Math.round(val * grow).toLocaleString("tr-TR")}
                {v.chart_unit ? ` ${v.chart_unit}` : ""}
              </span>
            </div>
            <div style={{ height: 48, background: "rgba(0,0,0,0.06)", border: ink.border(4), borderRadius: 24, overflow: "hidden" }}>
              <div style={{ height: "100%", width: `${(val / max) * 100 * grow}%`, background: accents[i % 4], borderRight: ink.border(4) }} />
            </div>
          </div>
        );
      })}
    </div>
  );
};

// Kod/terminal: yazma hızı, slot süresinin %65'inde bitecek şekilde ayarlanır; aktif satır vurgulu
export const CodeBlock: React.FC<{ v: Visual; terminal?: boolean; durationInFrames: number }> = ({ v, terminal, durationInFrames }) => {
  const frame = useCurrentFrame();
  const lines = v.code_lines ?? [];
  const total = lines.reduce((n, l) => n + l.length, 0);
  const typed = interpolate(frame, [6, Math.max(12, durationInFrames * 0.65)], [0, total], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  let budget = typed;
  return (
    <div style={{ ...cardStyle, ...useEnter(), background: "#14171f", color: "#e8eaed", padding: 0, overflow: "hidden" }}>
      <div style={{ display: "flex", gap: 14, padding: "26px 32px", borderBottom: "2px solid #2a2f3a", alignItems: "center" }}>
        {[colors.red, colors.yellow, colors.green].map((c) => (
          <div key={c} style={{ width: 24, height: 24, borderRadius: 12, background: c }} />
        ))}
        <span style={{ marginLeft: 16, fontSize: 30, color: "#9aa4b1" }}>{terminal ? "terminal" : v.code_language ?? "kod"}</span>
      </div>
      <div style={{ padding: "32px 40px", fontFamily: "Consolas, 'Courier New', monospace", fontSize: 40, lineHeight: 1.55 }}>
        {lines.map((line, i) => {
          const visible = line.slice(0, Math.max(0, Math.floor(budget)));
          const typing = budget > 0 && budget < line.length;
          budget -= line.length;
          return (
            <div key={i} style={{ whiteSpace: "pre-wrap", wordBreak: "break-all", minHeight: 62, background: typing ? "rgba(66,133,244,0.12)" : "transparent", margin: "0 -40px", padding: "0 40px" }}>
              {terminal && <span style={{ color: colors.green }}>$ </span>}
              <span style={{ color: terminal ? "#e8eaed" : "#c9d1d9" }}>{visible}</span>
              {typing && frame % 14 < 8 ? <span style={{ color: colors.blue }}>▍</span> : null}
            </div>
          );
        })}
      </div>
    </div>
  );
};

// Kaynak sayfa: perspektifli tarayıcı çerçevesi düzleşir, sayfa yavaşça kayar, başlık vurgulanır
export const SourceScreenshot: React.FC<{ v: Visual; durationInFrames: number; accent: string }> = ({ v, durationInFrames, accent }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const k = (width - 2 * 72) / 1080; // ekran görüntüsü 1080 px genişlikte alındı, kart genişliğine ölçeklenir
  const box = v.title_box;
  const s = spring({ frame, fps, config: { damping: 18, mass: 0.9 } });
  // Önce başlığa yakın plan (telefonda okunabilsin), sonra geri çekilip sayfa aşağı kayar
  const zoomEnd = Math.max(fps * 1.2, durationInFrames * 0.45);
  const zoom = interpolate(frame, [fps * 0.3, zoomEnd], [box ? 1.5 : 1.3, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const ox = box ? Math.max(0, box.x * k - 20) : (width - 2 * 72) / 2; // başlığın sol kenarı sabit: yakınlaşınca solu kesilmesin
  const oy = box ? (box.y + box.h / 2) * k : 0;
  const scroll = interpolate(frame, [zoomEnd, durationInFrames], [0, -220], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const mark = interpolate(frame, [fps * 0.5, fps * 1.1], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  if (!v.screenshot) return null;
  return (
    <div
      style={{
        width: "100%",
        transform: `perspective(1800px) rotateY(${(1 - s) * -28}deg) rotateX(${(1 - s) * 10}deg) translateY(${(1 - s) * 120}px) scale(${0.9 + 0.1 * s})`,
        opacity: Math.min(1, s * 1.5),
        borderRadius: 24,
        overflow: "hidden",
        border: ink.border(6),
        boxShadow: ink.shadow(16, accent),
        background: "#fff",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 12, padding: "18px 24px", background: colors.text }}>
        {[colors.red, colors.yellow, colors.green].map((c) => (
          <div key={c} style={{ width: 18, height: 18, borderRadius: 9, background: c }} />
        ))}
        <div style={{ flex: 1, marginLeft: 16, background: "#2b2b2b", borderRadius: 12, padding: "8px 20px", fontFamily, fontSize: 28, color: "#d9d4c9" }}>
          {v.domain}
        </div>
      </div>
      <div style={{ position: "relative", height: 780, overflow: "hidden" }}>
        <div style={{ position: "absolute", inset: 0, transform: `scale(${zoom})`, transformOrigin: `${ox}px ${oy}px` }}>
        <Img src={staticFile(v.screenshot)} style={{ width: "100%", transform: `translateY(${scroll}px)` }} />
        {/* Fosforlu kalem: Playwright'ın ölçtüğü makale başlığı (h1) kutusunun üstünden geçer */}
        {box ? (
          <div
            style={{
              position: "absolute",
              left: box.x * k - 8,
              top: box.y * k + scroll - 6,
              height: box.h * k + 12,
              width: (box.w * k + 16) * mark,
              background: `${colors.yellow}66`,
              mixBlendMode: "multiply",
              borderRadius: 8,
            }}
          />
        ) : null}
        </div>
      </div>
    </div>
  );
};

// İmza kartı: her bölümde aynı yerde, aynı (yeşil) renkte; metin kelime kelime gelir
export const StudentTakeCard: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const enter = useEnter();
  const words = text.split(" ");
  return (
    <div style={{ ...cardStyle, ...enter, background: "#DDF3E1", transform: `${enter.transform} rotate(-1.5deg)` }}>
      <div style={{ display: "inline-block", background: colors.green, color: onAccent(colors.green), border: ink.border(4), boxShadow: ink.shadow(5), fontSize: 32, fontWeight: 700, borderRadius: 12, padding: "4px 16px", marginBottom: 26 }}>
        SENİN İÇİN NE DEMEK?
      </div>
      <div style={{ fontSize: 58, fontWeight: 700, lineHeight: 1.22 }}>
        {words.map((w, i) => {
          const s = spring({ frame: frame - 6 - i * 2, fps, config: { damping: 14, mass: 0.4 } });
          return (
            <span key={i} style={{ display: "inline-block", marginRight: 16, opacity: s, transform: `translateY(${(1 - s) * 24}px)` }}>
              {w}
            </span>
          );
        })}
      </div>
    </div>
  );
};
