# Editable project cover

[cover.svg](cover.svg) is the editable source; [cover.png](cover.png) is the
1280 × 640 PNG used by the README (under 1 MB).

## Design and source

Trajectories and point density illustrate accumulated wrist-region motion. This is conceptual artwork, not a new heatmap, finger-landmark detection, or model run.

Text and geometry are editable SVG. Existing demo images, screenshots and animations
remain in their original files; only the cover composition changed.

## Export

Open the SVG in a browser or vector editor. It uses Segoe UI, Georgia, Consolas
and Noto Sans TC system fonts, so another computer may substitute fonts.
The PNG preserves the reviewed appearance. With Microsoft Edge installed:

```text
msedge --headless=new --disable-gpu --hide-scrollbars --window-size=1280,640 --screenshot=cover.png file:///absolute/path/to/cover.svg
```

Render into a scratch directory, inspect the full-size image and a 320 × 160
thumbnail, then replace the PNG beside the SVG. Keep all original demo files.
