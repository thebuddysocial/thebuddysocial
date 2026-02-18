# PRD - The Buddy Social Live Preview

## Original Problem Statement
Preview the current GitHub repo (thebuddysocial/thebuddysocial) netlify-deploy/index.html in live preview mode.

## Architecture
- **Frontend**: React app serving a full-viewport iframe to the static HTML page
- **Static Site**: Self-contained `index.html` (HTML + CSS + JS) from `netlify-deploy/`
- **Backend**: FastAPI (unchanged, not actively used for this task)
- **Database**: MongoDB (unchanged, not actively used)

## What's Been Implemented (2026-02-18)
- Cloned the `thebuddysocial/thebuddysocial` GitHub repo
- Copied `netlify-deploy/index.html` to `frontend/public/buddysocial.html`
- Modified `App.js` to render a full-viewport iframe pointing to `/buddysocial.html`
- Updated `App.css` to remove default boilerplate styles and ensure full-page iframe rendering
- All features working: GSAP animations, custom cursor, scroll effects, 3D tilt cards, navigation, CDN resources

## Site Features (from original repo)
- Responsive design (mobile + desktop)
- Custom cursor with hover effects
- GSAP scroll animations with ScrollTrigger
- 3D tilt effects on cards
- Auto-scrolling photo carousel
- Video hero background
- Photo-inside-text effect for "THE BUDDY SOCIAL"
- Premium gold accent styling

## External Dependencies (via CDN)
- Google Fonts (Bebas Neue, Playfair Display, DM Sans)
- Font Awesome 6.5.1
- GSAP 3.12.5 + ScrollTrigger

## Status
Live preview running at: https://github-viewer-live.preview.emergentagent.com

## Backlog
- P1: Any UI/content edits the user wants to make to the landing page
- P2: Connect backend for dynamic features (event management, ticket tracking, etc.)
