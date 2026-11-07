import { AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { CodeBlock, MiniChart, SourceScreenshot, StatCounter, StudentTakeCard } from "./components/Cards";
import { Agenda, FollowOutro, QuestionCTA } from "./components/Flow";
import { Hook } from "./components/Hook";
import { Camera, Grain, HeadlineChip, KeywordPunch, KineticCaptions, MotionBackground, SegmentIntro, keywordTimes, punchMoments } from "./components/Motion";
import { Logo, ProgressBar } from "./components/Overlay";
import { accents, colors, fontFamily, safe } from "./theme";
import type { EpisodeProps, Segment, Unit, Visual } from "./types";

const INTRO_S = 1.6; // haber geçişi (renk şeritleri + numara + başlık); köprü cümlesi uzunsa onun sonuna kadar sürer
const VISUAL_MIN_S = 2.4; // her görsel en az bu kadar kalır; ekranda 2-3 sn'de bir değişim olur

type Slot = { from: number; dur: number; render: (dur: number) => React.ReactNode };

// Görsel verisi olmayan haberler için yedek: büyük başlık kartı
const BigHeadline: React.FC<{ seg: Segment }> = ({ seg }) => {
  const frame = useCurrentFrame();
  const accent = accents[(seg.index - 1) % 4];
  const s = interpolate(frame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
  return (
    <div style={{ fontFamily, color: colors.text, opacity: s, borderLeft: `14px solid ${accent}`, paddingLeft: 40 }}>
      <div style={{ fontSize: 96, fontWeight: 700, lineHeight: 1.05, letterSpacing: -2 }}>{seg.headline}</div>
      <div style={{ fontSize: 36, color: colors.muted, marginTop: 24 }}>{seg.sourceLabel}</div>
    </div>
  );
};

function usable(v: Visual): boolean {
  switch (v.component) {
    case "SourceScreenshot":
      return Boolean(v.screenshot);
    case "StatCounter":
      return v.stat_value != null;
    case "MiniChart":
      return (v.chart_values?.length ?? 0) >= 2;
    case "CodeBlock":
    case "Terminal":
      return (v.code_lines?.length ?? 0) > 0;
    default:
      return false; // HeadlineCard'ın yerini haber geçişi aldı
  }
}

function segmentSlots(seg: Segment, introEnd: number, take: Unit, segEnd: number, fps: number): Slot[] {
  const f = (s: number) => Math.round(s * fps);
  const accent = accents[(seg.index - 1) % 4];
  const slots: Slot[] = [];
  const start = introEnd;
  const span = take.start - start;
  const items = seg.visuals.filter(usable);
  const n = items.length ? Math.max(1, Math.min(items.length, Math.floor(span / VISUAL_MIN_S))) : 1;
  for (let i = 0; i < n; i++) {
    const v = items[i];
    const from = f(start + (i * span) / n);
    const dur = f(start + ((i + 1) * span) / n) - from;
    slots.push({
      from,
      dur,
      render: (d) => {
        if (!v) return <BigHeadline seg={seg} />;
        switch (v.component) {
          case "StatCounter":
            return <StatCounter v={v} index={seg.index} />;
          case "MiniChart":
            return <MiniChart v={v} />;
          case "CodeBlock":
            return <CodeBlock v={v} durationInFrames={d} />;
          case "Terminal":
            return <CodeBlock v={v} terminal durationInFrames={d} />;
          default:
            return <SourceScreenshot v={v} durationInFrames={d} accent={accent} />;
        }
      },
    });
  }
  // "Senin için ne demek?" kartı: her bölümde aynı yerde
  slots.push({ from: f(take.start), dur: f(segEnd) - f(take.start), render: () => <StudentTakeCard text={seg.studentTake} /> });
  return slots;
}

const SegmentProgress: React.FC<{ index: number; total: number; durationInFrames: number }> = ({ index, total, durationInFrames }) => {
  const frame = useCurrentFrame();
  return <ProgressBar current={index} total={total} progress={Math.min(1, frame / durationInFrames)} />;
};

export const Episode: React.FC<EpisodeProps> = (p) => {
  const { fps, durationInFrames } = useVideoConfig();
  const f = (s: number) => Math.round(s * fps);
  const find = (id: string) => p.units.find((u) => u.id === id);
  const unit = (id: string) => find(id)!;
  const hook = unit("hook");
  const teaser = find("teaser");
  const question = find("question");
  const outro = unit("outro");
  // Haber, köprü cümlesiyle başlar (varsa); son haber yorum sorusuna kadar sürer
  const segStarts = p.segments.map((s) => (find(`s${s.index}_bridge`) ?? unit(`s${s.index}_narration`)).start);
  const tailStart = (question ?? outro).start;
  const segEnds = p.segments.map((_, i) => (i + 1 < segStarts.length ? segStarts[i + 1] : tailStart));
  const introEnds = p.segments.map((s, i) => Math.max(segStarts[i] + INTRO_S, unit(`s${s.index}_narration`).start + 0.35));
  const outroFrom = f(outro.start);
  const hits = keywordTimes(p.units);
  const accentFor = (u: Unit) => (u.segment ? accents[(u.segment - 1) % 4] : colors.yellow);
  // Sayaçta zaten büyük gösterilen rakam ayrıca kart olarak çakılmaz
  const statValues = Object.fromEntries(
    p.segments.map((s) => [s.index, s.visuals.filter((v) => v.component === "StatCounter").map((v) => String(v.stat_value))]),
  );
  const punches = punchMoments(p.units, statValues);
  const PUNCH_S = 1.0;

  // Anlatım sırasında müzik kısılır (ducking); konuşma arasında yumuşakça geri gelir
  const musicVolume = (frame: number) => {
    const t = frame / fps;
    const dist = Math.min(...p.units.map((u) => (t < u.start ? u.start - t : t > u.end ? t - u.end : 0)));
    const v = interpolate(dist, [0, 0.35], [p.duckVolume, p.musicVolume], { extrapolateRight: "clamp" });
    const fadeOut = interpolate(frame, [durationInFrames - fps, durationInFrames], [1, 0], { extrapolateLeft: "clamp" });
    return v * fadeOut;
  };

  return (
    <AbsoluteFill style={{ backgroundColor: colors.bg }}>
      <Audio src={staticFile(p.voice)} />
      <Audio src={staticFile(p.music)} volume={musicVolume} loop />

      <Camera hits={hits}>
        <MotionBackground accent={colors.yellow} />
        {p.segments.map((s, i) => (
          <Sequence key={`bg${i}`} from={f(segStarts[i])} durationInFrames={f(segEnds[i]) - f(segStarts[i])}>
            <MotionBackground accent={accents[i % 4]} />
          </Sequence>
        ))}

        {/* Kanca: 0. kareden itibaren, kelimeler seslendirildiği anda çakılır */}
        <Sequence from={0} durationInFrames={Math.max(f(teaser?.start ?? segStarts[0] ?? hook.end), 1)}>
          <Hook text={p.hook} words={hook.words} icon={p.segments[0]?.icon} />
        </Sequence>

        {/* Teaser: bu haftanın listesi, son haber kilitli */}
        {teaser && segStarts.length ? (
          <Sequence from={f(teaser.start)} durationInFrames={Math.max(f(segStarts[0]) - f(teaser.start), 1)}>
            <Agenda headlines={p.segments.map((s) => s.headline)} durationInFrames={Math.max(f(segStarts[0]) - f(teaser.start), 1)} />
          </Sequence>
        ) : null}

        {p.segments.map((seg, i) => {
          const take = unit(`s${seg.index}_take`);
          const segFrom = f(segStarts[i]);
          const segDur = f(segEnds[i]) - segFrom;
          const slots = segmentSlots(seg, introEnds[i], take, segEnds[i], fps);
          return (
            <Sequence key={seg.index} from={segFrom} durationInFrames={segDur}>
              {slots.map((sl, k) => (
                <Sequence key={k} from={sl.from - segFrom} durationInFrames={Math.max(sl.dur, 1)}>
                  <AbsoluteFill style={{ justifyContent: "center", padding: `0 ${safe.side}px`, paddingTop: 420, paddingBottom: 620 }}>
                    {sl.render(sl.dur)}
                  </AbsoluteFill>
                  <Audio src={staticFile(p.pop)} volume={0.22} endAt={Math.round(0.2 * fps)} />
                </Sequence>
              ))}
              <Sequence from={f(introEnds[i]) - segFrom - 6}>
                <HeadlineChip index={seg.index} headline={seg.headline} />
              </Sequence>
            </Sequence>
          );
        })}

        {punches.map((pu, k) => (
          <Sequence key={`pu${k}`} from={f(pu.t) - 2} durationInFrames={f(PUNCH_S)}>
            <KeywordPunch text={pu.text} sub={pu.sub} accent={accents[(pu.segment - 1) % 4]} durationInFrames={f(PUNCH_S)} />
            <Audio src={staticFile(p.whoosh)} volume={0.25} endAt={Math.round(0.35 * fps)} />
          </Sequence>
        ))}

        {question ? (
          <Sequence from={f(question.start)} durationInFrames={Math.max(outroFrom - f(question.start), 1)}>
            <QuestionCTA text={p.question ?? ""} words={question.words} startS={question.start} />
          </Sequence>
        ) : null}

        <Sequence from={outroFrom} durationInFrames={durationInFrames - outroFrom}>
          <FollowOutro text={p.outroText} logo={p.logo} handle={p.handle ?? ""} />
        </Sequence>
      </Camera>

      {/* Sabit katmanlar kameradan bağımsız: logo, rozet, ilerleme, altyazı */}
      {p.segments.map((seg, i) => (
        <Sequence key={`pr${i}`} from={f(segStarts[i])} durationInFrames={f(segEnds[i]) - f(segStarts[i])}>
          <SegmentProgress index={seg.index} total={p.segments.length} durationInFrames={f(segEnds[i]) - f(segStarts[i])} />
        </Sequence>
      ))}
      <KineticCaptions units={p.units} accentFor={accentFor} />

      {/* Haber geçişleri tüm katmanların üstünde */}
      {p.segments.map((seg, i) => (
        <Sequence key={`in${i}`} from={f(segStarts[i])} durationInFrames={f(introEnds[i]) - f(segStarts[i])}>
          <SegmentIntro
            index={seg.index}
            total={p.segments.length}
            headline={seg.headline}
            kicker={seg.bridge}
            icon={seg.icon}
            durationInFrames={f(introEnds[i]) - f(segStarts[i])}
          />
          <Audio src={staticFile(p.whoosh)} volume={0.55} />
        </Sequence>
      ))}
      {teaser ? (
        <Sequence from={f(teaser.start)}>
          <Audio src={staticFile(p.whoosh)} volume={0.4} />
        </Sequence>
      ) : null}
      {question ? (
        <Sequence from={f(question.start)}>
          <Audio src={staticFile(p.pop)} volume={0.5} endAt={Math.round(0.3 * fps)} />
        </Sequence>
      ) : null}
      <Sequence from={outroFrom}>
        <Audio src={staticFile(p.whoosh)} volume={0.5} />
      </Sequence>
      <Sequence from={outroFrom + Math.round(fps * 1.1)}>
        <Audio src={staticFile(p.pop)} volume={0.6} endAt={Math.round(0.3 * fps)} />
      </Sequence>

      <Sequence from={0} durationInFrames={outroFrom}>
        <Logo src={p.logo} />
      </Sequence>
      {/* "AI ile üretildi" artık videoda değil: Instagram'ın yükleme ekranındaki AI etiketiyle işaretlenir (post.md) */}
      <Grain />
    </AbsoluteFill>
  );
};
