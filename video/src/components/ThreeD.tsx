import { ThreeCanvas } from "@remotion/three";
import { useMemo } from "react";
import { spring, useCurrentFrame, useVideoConfig } from "remotion";
import { FontLoader } from "three/examples/jsm/loaders/FontLoader.js";
import { TextGeometry } from "three/examples/jsm/geometries/TextGeometry.js";
import helvetiker from "three/examples/fonts/helvetiker_bold.typeface.json";
import { colors } from "../theme";

// 3D vurgu parçaları (three.js): editoryal temanın üstünde yalnızca kancada ve büyük rakamlarda kullanılır;
// her sahnede 3D olursa o da şablon gibi durur. Font yalnızca ASCII içerir: rakam, %, nokta, virgül.
const font = new FontLoader().parse(helvetiker as never);
const CAM_Z = 9;
const FOV = 40;
// Kamera düzleminde (z=0) görünen genişlik, sahne birimiyle
const visibleWidth = (w: number, h: number) => 2 * CAM_Z * Math.tan(((FOV / 2) * Math.PI) / 180) * (w / h);

const Number3DMesh: React.FC<{ text: string; color: string; delay: number; maxWidth: number }> = ({ text, color, delay, maxWidth }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const geo = useMemo(() => {
    const g = new TextGeometry(text, { font, size: 2.4, depth: 0.9, bevelEnabled: true, bevelThickness: 0.12, bevelSize: 0.08, bevelSegments: 6, curveSegments: 16 });
    g.center();
    g.computeBoundingBox();
    return g;
  }, [text]);
  // Uzun sayılar ("1071", "16,3") kadraja sığsın: genişlik görünür alanın en fazla maxWidth'i kadar
  const box = geo.boundingBox!;
  const fit = Math.min(1, maxWidth / (box.max.x - box.min.x));
  const s = spring({ frame: frame - delay, fps, config: { damping: 11, mass: 0.7 } });
  // Önce yarım tur dönerek yerine oturur, sonra hafifçe salınır
  const spin = (1 - s) * Math.PI * 1.2 + Math.sin(frame / 22) * 0.35;
  return (
    <mesh geometry={geo} rotation={[0.18, spin, 0]} scale={fit * (0.3 + 0.7 * s)}>
      <meshPhysicalMaterial color={color} roughness={0.18} clearcoat={1} clearcoatRoughness={0.05} metalness={0.05} />
    </mesh>
  );
};

const Floaters: React.FC = () => {
  const frame = useCurrentFrame();
  const items: { c: string; p: [number, number, number]; s: number; kind: string }[] = [
    { c: colors.red, p: [-2.9, 2.0, -2], s: 0.45, kind: "sphere" },
    { c: colors.green, p: [2.9, -1.8, -1.5], s: 0.55, kind: "torus" },
    { c: colors.yellow, p: [2.6, 2.3, -3], s: 0.42, kind: "box" },
    { c: colors.blue, p: [-2.6, -2.2, -2.5], s: 0.45, kind: "box" },
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

const Lights: React.FC = () => (
  <>
    <ambientLight intensity={0.65} />
    <directionalLight position={[4, 6, 8]} intensity={2.2} />
    <directionalLight position={[-6, -2, 4]} intensity={0.7} color={colors.blue} />
  </>
);

// Parlak 3D rakam (+ istenirse etrafta yüzen Google renklerinde şekiller)
export const Number3D: React.FC<{ text: string; color: string; width: number; height: number; floaters?: boolean; delay?: number }> = ({
  text,
  color,
  width,
  height,
  floaters = false,
  delay = 0,
}) => (
  <ThreeCanvas width={width} height={height} camera={{ position: [0, 0, CAM_Z], fov: FOV }}>
    <Lights />
    <Number3DMesh text={text} color={color} delay={delay} maxWidth={visibleWidth(width, height) * 0.62} />
    {floaters ? <Floaters /> : null}
  </ThreeCanvas>
);

// Rakam yoksa (ör. kancada sayı geçmiyorsa) yalnızca yüzen şekiller
export const Floaters3D: React.FC<{ width: number; height: number }> = ({ width, height }) => (
  <ThreeCanvas width={width} height={height} camera={{ position: [0, 0, CAM_Z], fov: FOV }}>
    <Lights />
    <Floaters />
  </ThreeCanvas>
);

// Kanca metnindeki ilk sayı: rakam ya da "bir…on" (3D'ye çevrilecek değer)
const WORDS: Record<string, string> = { bir: "1", iki: "2", üç: "3", dört: "4", beş: "5", altı: "6", yedi: "7", sekiz: "8", dokuz: "9", on: "10" };
export function firstNumber(text: string): string | null {
  for (const raw of text.split(/\s+/)) {
    const w = raw.replace(/[^\p{L}\p{N}%.,]/gu, "").replace(/[.,]+$/, "");
    if (/^%?\d+([.,]\d+)?%?$/.test(w)) return w;
    const key = w.toLocaleLowerCase("tr");
    if (WORDS[key]) return WORDS[key];
  }
  return null;
}
