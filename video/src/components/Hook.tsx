import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { colors, fontFamily, ink, safe } from "../theme";
import type { Word } from "../types";
import { TopicIcon } from "./Icons";
import { Floaters3D, Number3D, firstNumber } from "./ThreeD";

// Açılış kancası: logo/intro yok. 0. karede üst yarıda 3D vurgu var: kancadaki sayı parlak 3D rakam olarak dönerek
// yerine oturur (sayı yoksa ilk haberin ikonu ve yüzen 3D şekiller). Kelimeler seslendirildiği anda büyükten
// "çakılır"; sayılar sarı çıkartma olarak patlar, her sayıda ve son kelimede ekran sarsılır.
export const Hook: React.FC<{ text: string; words: Word[]; icon?: string; accent?: string }> = ({ text, words: timed, icon, accent = colors.blue }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const words = text.split(" ");
  const num = firstNumber(text);
  const isNum = (w: string) => /\d/.test(w) || (num !== null && firstNumber(w) === num);
  const startOf = (i: number) => (timed[i] ? Math.round(timed[i].start * fps) : i * 4);
  const hits = words.map((w, i) => (isNum(w) || i === words.length - 1 ? startOf(i) : -1)).filter((h) => h >= 0 && h <= frame);
  const lastHit = hits.length ? hits[hits.length - 1] : -99;
  const shake = Math.exp(-(frame - lastHit) / 4) * 16;
  const flash = interpolate(frame - lastHit, [0, 2, 9], [0, 0.35, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const iconIn = spring({ frame, fps, config: { damping: 14 } });
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ background: colors.yellow, opacity: flash }} />
      <AbsoluteFill style={{ top: safe.top + 60, height: 720 }}>
        {num ? (
          <Number3D text={num} color={accent} width={width} height={720} floaters />
        ) : (
          <>
            <Floaters3D width={width} height={720} />
            <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", transform: `scale(${iconIn})` }}>
              <TopicIcon name={icon} size={340} color={colors.text} stroke={1.6} />
            </AbsoluteFill>
          </>
        )}
      </AbsoluteFill>
      <AbsoluteFill
        style={{
          justifyContent: "flex-end",
          padding: `0 ${safe.side}px`,
          paddingBottom: safe.bottom - 20, // 3D alanın (üstte 720 px) altında kalsın
          transform: `translate(${Math.sin(frame * 2.3) * shake}px, ${Math.cos(frame * 1.7) * shake}px)`,
        }}
      >
        <div style={{ fontFamily, fontWeight: 700, fontSize: 124, lineHeight: 1.08, color: colors.text, letterSpacing: -4, textAlign: "center" }}>
          {words.map((w, i) => {
            const s = i === 0 ? 1 : spring({ frame: frame - startOf(i), fps, config: { damping: 11, mass: 0.5 } });
            const n = isNum(w);
            const last = i === words.length - 1;
            return (
              <span
                key={i}
                style={{
                  display: "inline-block",
                  margin: "8px 14px",
                  opacity: Math.min(1, s * 2),
                  transform: `scale(${interpolate(s, [0, 1], [n ? 2.4 : 1.7, 1])}) rotate(${n ? -3 : 0}deg)`,
                  filter: `blur(${(1 - Math.min(1, s)) * 12}px)`,
                  background: n ? colors.yellow : "none",
                  border: n ? ink.border(6) : "none",
                  boxShadow: n ? ink.shadow(10) : "none",
                  borderRadius: n ? 18 : 0,
                  padding: n ? "0 22px" : 0,
                  // son kelime: fosforlu kalem altı çizgisi
                  backgroundImage: last && !n ? `linear-gradient(transparent 62%, ${colors.red}aa 62%)` : undefined,
                }}
              >
                {w}
              </span>
            );
          })}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
