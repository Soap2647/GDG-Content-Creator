import { AbsoluteFill, Img, staticFile } from "remotion";
import { Grain, MotionBackground } from "./components/Motion";
import { accents, colors, fontFamily, safe } from "./theme";
import type { EpisodeProps } from "./types";

// Kapak görseli: kanca + haber başlıkları. Şirket logosu/gerçek kişi fotoğrafı yok.
export const Thumbnail: React.FC<EpisodeProps> = ({ hook, segments, week, logo }) => (
  <AbsoluteFill style={{ fontFamily, color: colors.text }}>
    <MotionBackground accent={accents[0]} />
    <Grain />
    <AbsoluteFill style={{ padding: `${safe.top + 40}px ${safe.side}px`, justifyContent: "space-between" }}>
      <div>
        <div style={{ fontSize: 40, fontWeight: 500, color: colors.muted }}>Haftalık Teknoloji Gündemi · {week}</div>
        <div style={{ fontSize: 112, fontWeight: 700, lineHeight: 1.05, letterSpacing: -2, marginTop: 40 }}>{hook}</div>
      </div>
      <div style={{ marginBottom: 260 }}>
        {segments.map((s, i) => (
          <div key={i} style={{ display: "flex", gap: 24, alignItems: "center", marginTop: 26 }}>
            <div style={{ width: 20, height: 20, borderRadius: 10, background: accents[i % 4], flexShrink: 0 }} />
            <div style={{ fontSize: 48, fontWeight: 500 }}>{s.headline}</div>
          </div>
        ))}
        <div style={{ display: "flex", alignItems: "center", gap: 28, marginTop: 60 }}>
          {logo ? (
            <Img src={staticFile(logo)} style={{ height: 72 }} />
          ) : (
            <span style={{ fontSize: 40, fontWeight: 700 }}>GDG on Campus Kastamonu</span>
          )}
        </div>
      </div>
    </AbsoluteFill>
  </AbsoluteFill>
);
