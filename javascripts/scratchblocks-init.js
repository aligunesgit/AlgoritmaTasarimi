// Render <pre class="blocks"> as Scratch 3 blocks (Turkish block text, English as fallback).
// Material's instant navigation swaps pages without a reload, so re-render on every page change.
document$.subscribe(() => {
  scratchblocks.renderMatching("pre.blocks", {
    style: "scratch3",
    languages: ["tr", "en"],
    scale: 0.75,
  });
});
