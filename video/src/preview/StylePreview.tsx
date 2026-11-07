import { ThreeCanvas } from "@remotion/three";
import { AbsoluteFill, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { useMemo } from "react";
import * as THREE from "three";
import { FontLoader } from "three/examples/jsm/loaders/FontLoader.js";
import { TextGeometry } from "three/examples/jsm/geometries/TextGeometry.js";
import helvetiker from "three/examples/fonts/helvetiker_bold.typeface.json";
import { colors, fontFamily } from "../theme";

// Görsel yön denemesi (yalnızca karar için; bölüm render'ına girmez).
// A: "Editoryal" — krem kâğıt zemin, kalın siyah tipografi, sert gölgeli çıkartma etiketler (neo-brütalist).
// B: "3D" — aynı açık zemin, three.js ile parlak 3D rakam/şekiller, stüdyo ışığı.

const PAPER = "#F3EEE4";
const INK = "#111111";
const hard = (c = INK) => `10px 10px 0 ${c}`;

const PaperBg: React.FC = () => (
  <AbsoluteFill style={{ background: PAPER }}>
    <AbsoluteFill
      style={{
        opacity: 0.35,
        backgroundImage:
          "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3'/></filter><rect width='100%' height='100%' filter='url(%23n)' opacity='0.35'/></svg>\")",
      }}
    />
  </AbsoluteFill>
);

const Sticker: React.FC<{ bg: string; color?: string; rotate?: number; size?: number; children: React.ReactNode }> = ({
  bg,
  color = INK,
  rotate = -3,
  size = 44,
  children,
}) => (
  <span
    style={{
      display: "inline-block",
      background: bg,
      color,
      border: `5px solid ${INK}`,
      boxShadow: hard(),
      borderRadius: 14,
      padding: "6px 22px",
      fontSize: size,
      fontWeight: 700,
      transform: `rotate(${rotate}deg)`,
    }}
  >
    {children}
  </span>
);

// A1: kanca sahnesi
export const StyleAHook: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: frame - 4, fps, config: { damping: 12 } });
  return (
    <AbsoluteFill style={{ fontFamily, color: INK }}>
      <PaperBg />
      <AbsoluteFill style={{ padding: "220px 80px", justifyContent: "center" }}>
        <Sticker bg={colors.yellow} rotate={-4}>BU HAFTA · 4 HABER</Sticker>
        <div style={{ fontSize: 150, fontWeight: 700, lineHeight: 0.98, letterSpacing: -6, marginTop: 50 }}>
          Google hesabınla ayda{" "}
          <span style={{ display: "inline-block", background: colors.blue, color: "#fff", padding: "0 24px", border: `6px solid ${INK}`, boxShadow: hard(), transform: `rotate(-2deg) scale(${0.6 + 0.4 * s})` }}>
            üç
          </span>{" "}
          yapay zeka videosu{" "}
          <span style={{ textDecoration: `underline ${colors.red}`, textDecorationThickness: 18, textUnderlineOffset: 14 }}>ücretsiz!</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// A2: haber sahnesi (ekran görüntüsü + etiketler)
export const StyleAStory: React.FC = () => (
  <AbsoluteFill style={{ fontFamily, color: INK }}>
    <PaperBg />
    <AbsoluteFill style={{ padding: "150px 72px" }}>
      <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
        <Sticker bg={colors.blue} color="#fff" rotate={0} size={40}>01</Sticker>
        <div style={{ fontSize: 46, fontWeight: 700 }}>Google Vids'te ücretsiz video</div>
      </div>
      <div style={{ marginTop: 70, border: `6px solid ${INK}`, boxShadow: hard(), borderRadius: 24, overflow: "hidden", background: "#fff", transform: "rotate(1.5deg)" }}>
        <div style={{ background: INK, color: PAPER, fontSize: 28, padding: "12px 24px" }}>blog.google</div>
        <div style={{ height: 760, overflow: "hidden" }}>
          <Img src={staticFile("screenshots/137f54d08c5c.png")} style={{ width: "100%" }} />
        </div>
      </div>
      <div style={{ marginTop: -60, marginLeft: 40 }}>
        <Sticker bg={colors.yellow} rotate={-5} size={84}>3 video / ay</Sticker>
      </div>
    </AbsoluteFill>
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 300 }}>
      <div style={{ fontSize: 76, fontWeight: 700, background: INK, color: PAPER, padding: "4px 24px" }}>
        ayda en fazla <span style={{ color: colors.yellow }}>3 adet</span>
      </div>
    </AbsoluteFill>
  </AbsoluteFill>
);

// B: three.js — parlak 3D rakam, yavaşça döner; arkada Google renklerinde yüzen şekiller
const Digit3D: React.FC<{ text: string; color: string }> = ({ text, color }) => {
  const frame = useCurrentFrame();
  const geo = useMemo(() => {
    const font = new FontLoader().parse(helvetiker as never);
    const g = new TextGeometry(text, { font, size: 2.4, depth: 0.8, bevelEnabled: true, bevelThickness: 0.12, bevelSize: 0.08, bevelSegments: 6, curveSegments: 16 });
    g.center();
    return g;
  }, [text]);
  return (
    <mesh geometry={geo} rotation={[0.15, Math.sin(frame / 25) * 0.6, 0]}>
      <meshPhysicalMaterial color={color} roughness={0.15} clearcoat={1} clearcoatRoughness={0.05} metalness={0.1} />
    </mesh>
  );
};

const Floaters: React.FC = () => {
  const frame = useCurrentFrame();
  const items = [
    { c: colors.red, p: [-2.6, 2.4, -2], s: 0.5, kind: "sphere" },
    { c: colors.green, p: [2.7, -2.2, -1.5], s: 0.6, kind: "torus" },
    { c: colors.yellow, p: [2.4, 2.8, -3], s: 0.45, kind: "box" },
    { c: colors.blue, p: [-2.4, -2.8, -2.5], s: 0.5, kind: "box" },
  ];
  return (
    <>
      {items.map((it, i) => (
        <mesh key={i} position={[it.p[0], it.p[1] + Math.sin(frame / 20 + i) * 0.15, it.p[2]]} rotation={[frame / 40 + i, frame / 30, 0]} scale={it.s}>
          {it.kind === "sphere" ? <sphereGeometry args={[1, 48, 48]} /> : it.kind === "torus" ? <torusGeometry args={[0.8, 0.32, 32, 64]} /> : <boxGeometry args={[1.2, 1.2, 1.2]} />}
          <meshPhysicalMaterial color={it.c} roughness={0.2} clearcoat={1} />
        </mesh>
      ))}
    </>
  );
};

export const StyleBHook: React.FC = () => {
  const { width, height } = useVideoConfig();
  const frame = useCurrentFrame();
  const s = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ fontFamily, color: INK }}>
      <AbsoluteFill style={{ background: `radial-gradient(circle at 50% 35%, #ffffff, ${PAPER} 70%)` }} />
      <AbsoluteFill style={{ height: 1150 }}>
        <ThreeCanvas width={width} height={1150} camera={{ position: [0, 0, 9], fov: 40 }}>
          <ambientLight intensity={0.6} />
          <directionalLight position={[4, 6, 8]} intensity={2.2} />
          <directionalLight position={[-6, -2, 4]} intensity={0.8} color={colors.blue} />
          <Digit3D text="3" color={colors.blue} />
          <Floaters />
        </ThreeCanvas>
      </AbsoluteFill>
      <AbsoluteFill style={{ justifyContent: "flex-end", padding: "0 80px", paddingBottom: 380, opacity: s }}>
        <div style={{ fontSize: 108, fontWeight: 700, lineHeight: 1.02, letterSpacing: -4, textAlign: "center" }}>
          Google hesabınla ayda üç yapay zeka videosu <span style={{ color: colors.blue }}>ücretsiz!</span>
        </div>
      </AbsoluteFill>
      <div style={{ position: "absolute", top: 0, height }} />
    </AbsoluteFill>
  );
};

export const StyleBStory: React.FC = () => {
  const { width } = useVideoConfig();
  return (
    <AbsoluteFill style={{ fontFamily, color: INK }}>
      <AbsoluteFill style={{ background: `radial-gradient(circle at 50% 30%, #ffffff, ${PAPER} 70%)` }} />
      <AbsoluteFill style={{ top: 180, height: 700 }}>
        <ThreeCanvas width={width} height={700} camera={{ position: [0, 0, 8], fov: 40 }}>
          <ambientLight intensity={0.6} />
          <directionalLight position={[4, 6, 8]} intensity={2.2} />
          <Digit3D text="16" color={colors.green} />
        </ThreeCanvas>
      </AbsoluteFill>
      <AbsoluteFill style={{ padding: "0 80px", top: 900 }}>
        <div style={{ fontSize: 40, fontWeight: 700, color: colors.green, letterSpacing: 4 }}>04 · SONA SAKLADIĞIMIZ</div>
        <div style={{ fontSize: 96, fontWeight: 700, lineHeight: 1.02, letterSpacing: -3, marginTop: 16 }}>TÜBİTAK STAR: son başvuru 16 Kasım</div>
        <div style={{ fontSize: 44, color: "#555", marginTop: 24 }}>saat 17.30 · lisans öğrencilerine burs</div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
