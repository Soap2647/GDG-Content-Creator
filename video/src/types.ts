// Python tarafındaki media adımının ürettiği render_props.json ile birebir aynı şekil.

export type Word = { text: string; start: number; end: number };

export type Unit = {
  id: string;
  kind: "hook" | "teaser" | "bridge" | "narration" | "take" | "question" | "outro";
  segment: number | null;
  start: number;
  end: number;
  words: Word[];
};

export type Visual = {
  component: "HeadlineCard" | "StatCounter" | "MiniChart" | "CodeBlock" | "Terminal" | "SourceScreenshot";
  stat_value?: number | null;
  stat_prefix?: string | null;
  stat_suffix?: string | null;
  stat_label?: string | null;
  chart_title?: string | null;
  chart_labels?: string[] | null;
  chart_values?: number[] | null;
  chart_unit?: string | null;
  code_language?: string | null;
  code_lines?: string[] | null;
  screenshot_url?: string | null;
  screenshot?: string | null; // public dir'e göre yerel dosya (media adımı doldurur)
  title_box?: { x: number; y: number; w: number; h: number } | null; // ekran görüntüsündeki makale başlığı (px, 1080 genişlik)
  domain?: string | null;
};

export type Segment = {
  index: number;
  headline: string;
  studentTake: string;
  bridge?: string; // haberden önce söylenen bağlaç cümlesi
  sourceLabel: string; // ör. "Kaynak: github.blog"
  icon?: string; // konu ikonu (components/Icons.tsx), media adımı metinden seçer
  visuals: Visual[];
};

export type EpisodeProps = {
  week: string;
  fps: number;
  durationInFrames: number;
  voice: string;
  music: string;
  whoosh: string;
  pop: string;
  logo: string | null;
  hook: string;
  outroText: string;
  outroSeconds: number;
  teaser?: string;
  question?: string;
  handle?: string; // Instagram kullanıcı adı (kapanıştaki takip çağrısı)
  units: Unit[];
  segments: Segment[];
  musicVolume: number;
  duckVolume: number;
};
