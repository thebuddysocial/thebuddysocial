# PRD - The Buddy Social Live Preview

## Original Problem Statement
Preview the GitHub repo (thebuddysocial/thebuddysocial) netlify-deploy/index.html in live preview mode with iterative design improvements.

## Architecture
- **Frontend**: React app serving full-viewport iframe to static HTML
- **Static Site**: `buddysocial.html` in `frontend/public/`
- **Backend**: FastAPI (unchanged)
- **Database**: MongoDB (unchanged)

## What's Been Implemented

### Phase 1 (2026-02-18) - Initial Setup
- Cloned repo, deployed as live preview via iframe

### Phase 2 (2026-02-18) - Content & Design Updates
1. Section 2 Photos: Replaced 5 stock photos with user's event photos
2. Services Section: Redesigned into premium numbered cards (01, 02, 03)
3. "Our Why" Spacing: Reduced excessive padding/margins

### Phase 3 (2026-02-18) - Carousel & Seamless Sections
1. **Carousel Expansion**: Added 5 new event photos interleaved between 4 existing images (9 unique, 18 total with loop duplicates). Slowed animation to 50s.
2. **Seamless Section Flow**: Unified all cream sections to same `var(--cream)` background, eliminating visible color-band section dividers. Added gradient transitions (cream-to-dark) at section boundaries using ::before/::after pseudo-elements on marquee, carousel wrapper, and Our Why section. Removed footer border-top.

## Backlog
- P1: Replace stock service images with user's own photos
- P2: Dynamic content via backend (event management, contact form)
- P2: Mobile responsiveness fine-tuning
