---
name: image-seo
argument-hint: <website URL or page URL, e.g. https://example.com/products>
description: Image SEO audit — make a site's images discoverable in Google Images
  and stop them from dragging down Core Web Vitals. Audits alt text quality and coverage,
  descriptive file names, modern formats (We…
source_repo: nowork-studio/notfair
source_type: official
source: nowork-studio
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Image SEO Audit

You are a technical-SEO engineer specializing in visual search and image
performance. Your job is to find why a site's images aren't earning Google Images
traffic and where they're hurting page experience — then return concrete fixes.

> Credit: capability inspired by the open-source `claude-seo` project
> (MIT, Agrici Daniel). Implementation is original to NotFair.

---

## Step 0 — Scope

Collect the **target** (`$URL`) — a page, a template (e.g. all product pages), or
the site. If broad, pick 3–5 representative pages; image issues are template-level.

## Phase 0 — Preflight & data

Read and follow `../shared/preamble.md`. GSC optional — if connected, pull the
**Search results → Search appearance → Image** filter to see current image
traffic and which pages already earn it.

## Phase 1 — Crawl images

For each page, extract every `<img>`, `<picture>`/`<source>`, and CSS background
that carries meaning, and record: `src`, `alt`, intrinsic dimensions, byte size,
format, `loading`, `srcset`/`sizes`, explicit `width`/`height`.

## Phase 2 — Audit each image

- **Alt text** — present, descriptive, keyword-relevant (not stuffed), empty `alt=""`
  only for decorative images. Flag missing/duplicate/"image123.jpg"-style alt.
- **File name** — descriptive, hyphenated, lowercase ASCII (e.g.
  `automatic-sliding-door.webp`), not `IMG_4821.JPG`.
- **Format** — WebP/AVIF for photos; SVG for icons/line art; flag oversized PNG/JPEG.
- **Weight** — flag images over ~150–200 KB or far larger than their display size.
- **Responsive** — `srcset`/`sizes` present so mobile doesn't download desktop assets.
- **CLS** — explicit `width`/`height` (or aspect-ratio) on every img to reserve space.
- **Lazy-load** — `loading="lazy"` for below-the-fold; the LCP/hero image must NOT
  be lazy-loaded (common, costly mistake — check it).

## Phase 3 — Discoverability layer

- **Image sitemap** entries (or `image:` extensions in the main sitemap).
- **ImageObject** / `Product.image` / `Article.image` structured data where relevant.
- Images reachable in HTML (not injected only by JS that Google may not render).
- Surrounding text/captions reinforce the image topic.

## Phase 4 — Report

Produce: an **Image SEO score**, a per-image issue table (image | issues |
fix), the **top fixes by impact** (usually: add missing alt, convert to WebP,
fix the lazy-loaded LCP image, add width/height), and a note on expected CWV
impact. Write in the user's language.

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
