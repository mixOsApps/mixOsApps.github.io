# mixOsApps.github.io

Developer site for **mixOsApps**, served at <https://mixosapps.github.io/>.

It exists for three reasons:

1. **`app-ads.txt`** — required by AdMob to verify authorized sellers of the app's ad
   inventory. It must sit at the domain **root**, which is why this repo has to be named
   `mixOsApps.github.io` (a user site) rather than being a project site.
2. **Developer website** — the URL declared in the Play Console store listing
   (Grow users -> Store presence -> Store settings -> Store listing contact details).
3. **Privacy policy** — `privacy.html`, so the policy is no longer served from a gist.

## Coexistence with the web prototype

This is a *user* site, so it serves the domain root. The separate `salah-app` repo is a
*project* site and keeps serving `https://mixosapps.github.io/salah-app/`. Adding this repo
does not affect it.

## Do not break app-ads.txt

- Keep `app-ads.txt` at the repo root, reachable at `/app-ads.txt`.
- It must return HTTP 200 as `text/plain`. No redirects, no HTML wrapper.
- Do not add a `robots.txt` that disallows crawlers.
- `.nojekyll` is present so GitHub Pages serves files verbatim without Jekyll processing.

Verify after any change:

    curl -sI https://mixosapps.github.io/app-ads.txt | head -3
