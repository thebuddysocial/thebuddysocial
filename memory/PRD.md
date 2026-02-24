# PRD - The Buddy Social Live Preview

## Original Problem Statement
Pull GitHub repo (https://github.com/thebuddysocial/thebuddysocial, branch: Version-02) and set up for live editing. Static website for Dublin community events.

## Architecture
- **Frontend**: React app (CRA + Craco) serving `buddysocial.html` via iframe
- **Static Site**: `buddysocial.html` in `/app/frontend/public/` (mirrored to `netlify-deploy/index.html`)
- **Deployment**: Netlify via GitHub (netlify-deploy/index.html + _headers)
- **3rd Party**: Cal.com scheduling (popup mode), GSAP animations (deferred), Font Awesome icons (async)

## Key Files
- `/app/frontend/public/buddysocial.html` - Main website HTML
- `/app/netlify-deploy/index.html` - Netlify deployment version (keep in sync)
- `/app/netlify-deploy/_headers` - Netlify caching/security headers

## What's Been Implemented

### Sessions 1-6: Setup, featured card, countdown, schedule title, founder LinkedIn overlays/badges, glitch fix, carousel speed, Cal.com popup, mobile About Us, Schedule nav fix

### Session 7: Performance Optimization (2026-02-24)
**Render-blocking fixes:**
- Moved GSAP (gsap.min.js + ScrollTrigger.min.js) from `<head>` to end of `<body>` with `defer` — saves ~3.5s
- Font Awesome CSS loaded async via `media="print" onload` pattern
- Wrapped GSAP-dependent code in `window.addEventListener('load')` 

**Image optimization:**
- 36 images now have `loading="lazy"` + `decoding="async"`
- 39 images have explicit `width` + `height` (prevents CLS)
- LCP logo gets `fetchpriority="high"` + preload link in head
- Nav logo: no lazy (above fold), but still has decoding="async"
- Pexels images downsized from w=1600 to w=800

**CSS performance:**
- `content-visibility: auto` on 4 offscreen sections (services, carousel, history, schedule)
- `will-change: transform` on carousel track (GPU-accelerated)
- `contain: layout style` on carousel section

**Network/caching:**
- 4 preconnect hints (Google Fonts, gstatic, emergentagent, cdnjs)
- Preload LCP logo image
- Netlify `_headers` with 1-year immutable cache for all static assets

**Video optimization:**
- Hero video: `preload="auto"` (above fold)
- Below-fold video: `preload="metadata"` (unchanged)

**Expected PSI improvements:**
- Render-blocking savings: ~3.5s (GSAP + FA deferred)
- Image lazy loading: ~50MB deferred from initial load
- CLS reduction: explicit dimensions on all images
- Caching: 108MB potential savings for repeat visits

## Pending / Backlog
- P0: Re-run PSI after Netlify deploy to verify scores
- P1: Replace stock service images with real photos (reduce payload further)
- P1: Convert images to WebP/AVIF (requires re-uploading to CDN)
- P2: Full mobile responsive audit
