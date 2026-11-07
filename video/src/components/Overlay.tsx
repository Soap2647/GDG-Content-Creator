import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { accents, colors, fontFamily, safe } from "../theme";
import type { Unit, Word } from "../types";

// Üstte "Haber 2/4" göstergesi
export const ProgressBar: React.FC<{ current: number; total: number; progress: number }> = ({ current, total, progress }) => (
  <div style={{ position: "absolute", top: safe.top + 100, left: safe.side, right: safe.side, display: "flex", gap: 10 }}>
    {Array.from({ length: total }, (_, i) => (
      <div key={i} style={{ flex: 1, height: 14, borderRadius: 7, background: "rgba(0,0,0,0.06)", border: "3px solid #111111", overflow: "hidden" }}>
        <div style={{ height: "100%", width: `${i < current - 1 ? 100 : i === current - 1 ? progress * 100 : 0}%`, background: accents[i % 4] }} />
      </div>
    ))}
  </div>
);

// GDG Kastamonu logosu: kapanış dışında video boyunca sol üstte sabit
export const Logo: React.FC<{ src: string | null }> = ({ src }) =>
  src ? (
    <Img src={staticFile(src)} style={{ position: "absolute", top: safe.top - 4, left: safe.side, height: 64 }} />
  ) : (
    <div style={{ position: "absolute", top: safe.top, left: safe.side, fontFamily, fontSize: 34, fontWeight: 700, color: colors.text }}>
      <span style={{ color: colors.blue }}>G</span>
      <span style={{ color: colors.red }}>D</span>
      <span style={{ color: colors.yellow }}>G</span> Kastamonu
    </div>
  );

// Koyu arka plan + yavaş kayan renk lekeleri (ekranda sürekli hafif hareket)
export const Background: React.FC<{ accent: string }> = ({ accent }) => {
  const frame = useCurrentFrame();
  const x = interpolate(Math.sin(frame / 90), [-1, 1], [20, 80]);
  const y = interpolate(Math.cos(frame / 110), [-1, 1], [25, 70]);
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(900px circle at ${x}% ${y}%, ${accent}33, transparent 60%), linear-gradient(180deg, ${colors.bg2}, ${colors.bg})`,
      }}
    />
  );
};

// Kapanış: GDG yazısı/logosu + etkinlik çağrısı (3 sn)
export const Outro: React.FC<{ text: string; logo: string | null }> = ({ text, logo }) => {
  const frame = useCurrentFrame();
  const s = interpolate(frame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", fontFamily, color: colors.text, opacity: s, paddingBottom: 200 }}>
      {logo ? (
        <Img src={staticFile(logo)} style={{ width: 640 }} />
      ) : (
        <div style={{ textAlign: "center" }}>
          <div style={{ fontSize: 120, fontWeight: 700, letterSpacing: -2 }}>
            <span style={{ color: colors.blue }}>G</span>
            <span style={{ color: colors.red }}>D</span>
            <span style={{ color: colors.yellow }}>G</span>
          </div>
          <div style={{ fontSize: 52, fontWeight: 500 }}>on Campus Kastamonu</div>
        </div>
      )}
      <div style={{ fontSize: 46, marginTop: 60, textAlign: "center", padding: "0 80px" }}>{text}</div>
      <div style={{ fontSize: 40, marginTop: 28, color: colors.green, fontWeight: 700 }}>Etkinlikler ve kayıt linki bio'da</div>
    </AbsoluteFill>
  );
};
