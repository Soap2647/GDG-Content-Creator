import { loadFont } from "@remotion/google-fonts/GoogleSans";

// Tek font ailesi: Google Sans (Türkçe karakterler için latin-ext)
export const { fontFamily } = loadFont("normal", {
  weights: ["400", "500", "700"],
  subsets: ["latin", "latin-ext"],
});

// 2026-11-07: "editoryal" tema. Koyu zemin + neon parlama ilk yapay zeka sitelerini andırıyordu; yerine krem kâğıt
// zemin, siyah mürekkep yazı, kalın siyah çerçeve ve sert (bulanıksız) gölgeli "çıkartma" kartlar.
export const colors = {
  bg: "#F3EEE4", // kâğıt
  bg2: "#E9E2D4",
  card: "#FFFFFF",
  cardBorder: "#111111",
  text: "#111111", // mürekkep
  muted: "#5E5A52",
  blue: "#1A73E8",
  red: "#EA4335",
  yellow: "#FBBC05",
  green: "#34A853",
};

export const accents = [colors.blue, colors.red, colors.yellow, colors.green];

// Vurgu renginin üstündeki yazı rengi (sarı/yeşil üstünde siyah, mavi/kırmızı üstünde beyaz)
export const onAccent = (c: string) => (c === colors.yellow || c === colors.green ? colors.text : "#FFFFFF");

// Çıkartma stili: kalın siyah çerçeve + sert ofset gölge
export const ink = {
  border: (w = 5) => `${w}px solid ${colors.text}`,
  shadow: (d = 10, c = colors.text) => `${d}px ${d}px 0 ${c}`,
};

// Kısa video arayüzleri (Shorts/Reels) altta ve sağda buton gösterir: içerik bu güvenli alanda kalır
export const safe = { top: 80, side: 72, bottom: 360 };
