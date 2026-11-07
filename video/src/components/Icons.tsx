import { interpolate, useCurrentFrame } from "remotion";

// Haber konusu ikonları: ekipçe çizilmiş basit çizgi ikonlar (marka/şirket logosu değil).
// media adımı haberin metninden anahtar kelimeyle seçer (media/run.py → ICON_RULES).
const PATHS: Record<string, string[]> = {
  lock: ["M7 11V8a5 5 0 0 1 10 0v3", "M5 11h14v10H5z", "M12 15v3"],
  flag: ["M5 21V4", "M5 4h11l-2 4 2 4H5"],
  globe: ["M12 3a9 9 0 1 0 0 18a9 9 0 1 0 0-18", "M3 12h18", "M12 3c3 3.2 3 14.8 0 18", "M12 3c-3 3.2-3 14.8 0 18"],
  calendar: ["M4 6h16v15H4z", "M4 10h16", "M8 3v5", "M16 3v5", "M8 14h3v3H8z"],
  chip: ["M7 7h10v10H7z", "M10 10h4v4h-4z", "M9 3v4", "M15 3v4", "M9 17v4", "M15 17v4", "M3 9h4", "M3 15h4", "M17 9h4", "M17 15h4"],
  code: ["M8 7l-5 5 5 5", "M16 7l5 5-5 5", "M14 4l-4 16"],
  shield: ["M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z", "M9 12l2 2 4-4"],
  rocket: ["M12 3c4 2 6 6 6 10l-3 3H9l-3-3c0-4 2-8 6-10z", "M12 9a1.5 1.5 0 1 0 0 3a1.5 1.5 0 1 0 0-3", "M9 16l-2 5 3-2", "M15 16l2 5-3-2"],
  phone: ["M8 3h8v18H8z", "M11 18h2"],
  spark: ["M12 3l2 6 6 2-6 2-2 6-2-6-6-2 6-2z", "M19 3v4", "M17 5h4"],
  bolt: ["M13 3L5 13h6l-1 8 8-10h-6z"],
};

// Çizgiler sırayla "çizilir" (stroke-dashoffset), sonra hafifçe nefes alır
export const TopicIcon: React.FC<{ name?: string; size: number; color: string; delay?: number; stroke?: number }> = ({
  name,
  size,
  color,
  delay = 0,
  stroke = 1.6,
}) => {
  const frame = useCurrentFrame() - delay;
  const paths = PATHS[name ?? ""] ?? PATHS.bolt;
  const breathe = 1 + 0.03 * Math.sin(frame / 9);
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" style={{ transform: `scale(${breathe})`, overflow: "visible" }}>
      {paths.map((d, i) => {
        const p = interpolate(frame, [i * 3 - 2, i * 3 + 10], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
        return (
          <path
            key={i}
            d={d}
            pathLength={1}
            stroke={color}
            strokeWidth={stroke}
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeDasharray={1}
            strokeDashoffset={p}
            style={{ filter: `drop-shadow(0 0 6px ${color}88)` }}
          />
        );
      })}
    </svg>
  );
};
