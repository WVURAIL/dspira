# WVU Design System assets

These files are built from the official [WVU Design System 3 Hugo source](https://github.com/wvuweb/wvu-ds-v3-hugo/tree/47f2647e578c5b66231c8e7b393017f6d73a02c1).
Commit: `47f2647e578c5b66231c8e7b393017f6d73a02c1`.

The public stylesheet and navigation endpoints returned HTTP 403 during the
September 23, 2026 audit. Serving pinned copies keeps the layout and keyboard
navigation available without depending on those endpoints. The upstream
source is unchanged. The Adobe font kit remains external.

To reproduce, check out that commit, then run from its root with Node.js 22:

```sh
npm install --no-save sass@1.105.0 esbuild@0.28.2
npx sass --quiet --style=compressed --no-source-map assets/scss/main.scss site.min.css
npx esbuild assets/js/meom-wvu-site-navigation--custom.js --bundle --minify --alias:js=./assets/js --outfile=navigation.min.js
```

Copy both outputs and the upstream LICENSE here. Update the lab and lessons
repositories together, then rebuild the combined preview and rerun the browser
accessibility and layout checks.

SHA-256:

- `site.min.css`: `5f62f1a3167f1f52005fc22aac565ef377209886ea7478a91af363a0f546afb8`
- `navigation.min.js`: `f2ff7532fa7f8ed532fb265fc54c3f39bfa50ec6fb839e9be2b461003cdff5cf`

The root `favicon.ico` and `favicon-wvu.ico` are copies of `static/favicon.ico`
from the same upstream commit. Pages use the new filename to refresh cached icons.
