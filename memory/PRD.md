# PRD - The Buddy Social Live Preview

## Original Problem Statement
Preview the GitHub repo (thebuddysocial/thebuddysocial) netlify-deploy/index.html in live preview mode. Then make 3 changes: replace Section 2 photos with user's uploaded event photos, redesign services section with creative format, and fix "Our Why" spacing.

## Architecture
- **Frontend**: React app serving a full-viewport iframe to static HTML
- **Static Site**: Self-contained `buddysocial.html` in `frontend/public/`
- **Backend**: FastAPI (unchanged, not actively used)
- **Database**: MongoDB (unchanged)

## What's Been Implemented

### Phase 1 (2026-02-18) - Initial Setup
- Cloned `thebuddysocial/thebuddysocial` GitHub repo
- Deployed `netlify-deploy/index.html` as live preview via iframe

### Phase 2 (2026-02-18) - Content & Design Updates
1. **Section 2 Photos**: Replaced 5 Pexels stock photos with user's actual event photos (customer-assets URLs)
2. **Services Section Redesign**: Transformed simple list items into premium numbered cards (01, 02, 03) with:
   - Large display-font numbers with subtle opacity
   - Bebas Neue headings with gold-accent hover bars
   - Arrow indicators on hover
   - Clean divider lines between items
3. **"Our Why" Spacing Fix**: Reduced padding from 6rem/8rem to 4rem, hero margin from 5rem to 2.5rem, stats header margin from 3rem to 1.5rem

## Backlog
- P1: Replace stock service images with user's actual photos
- P2: Add more event details / dynamic content
- P2: Connect backend for contact form, event management
