import { Composition } from "remotion";
import { Episode } from "./Episode";
import { Thumbnail } from "./Thumbnail";
import { StyleAHook, StyleAStory, StyleBHook, StyleBStory } from "./preview/StylePreview";
import type { EpisodeProps } from "./types";

// Studio'da önizleme için örnek; gerçek render'da props episodes/<week>/render_props.json'dan gelir.
const sample: EpisodeProps = {
  week: "2026-W00",
  fps: 30,
  durationInFrames: 300,
  voice: "audio/voice.wav",
  music: "media/bed.mp3",
  whoosh: "media/whoosh.mp3",
  pop: "media/pop.mp3",
  logo: null,
  hook: "Örnek kanca cümlesi burada",
  outroText: "Haftaya görüşmek üzere!",
  outroSeconds: 3,
  units: [],
  segments: [],
  musicVolume: 0.18,
  duckVolume: 0.06,
};

export const Root: React.FC = () => (
  <>
    <Composition
      id="Episode"
      component={Episode}
      width={1080}
      height={1920}
      fps={30}
      durationInFrames={300}
      defaultProps={sample}
      calculateMetadata={({ props }) => ({ durationInFrames: props.durationInFrames, fps: props.fps })}
    />
    {/* Görsel yön denemeleri (karar için) */}
    <Composition id="StyleAHook" component={StyleAHook} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="StyleAStory" component={StyleAStory} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="StyleBHook" component={StyleBHook} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="StyleBStory" component={StyleBStory} width={1080} height={1920} fps={30} durationInFrames={60} />
    <Composition id="Thumbnail" component={Thumbnail} width={1080} height={1920} fps={30} durationInFrames={1} defaultProps={sample} />
  </>
);
