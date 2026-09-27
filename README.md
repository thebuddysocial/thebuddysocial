# The Buddy Social

Website for [The Buddy Social](https://thebuddysocial.com) — a Dublin community running monthly events for students, graduates, and early-career professionals.

## What's here

This is a single static HTML file — no build step, no framework. All CSS and JS are inline in the page.

- `netlify-deploy/index.html` — the entire site
- `netlify-deploy/_headers` — Netlify caching & security headers

## Deployment

This branch (`Version-02`) is connected to Netlify for continuous deployment. Pushing to this branch automatically builds and deploys to [thebuddysocial.com](https://thebuddysocial.com), publishing the `netlify-deploy/` directory.

To make a change: edit `netlify-deploy/index.html` directly, commit, and push to `Version-02`.

> Note: the `main` branch is not connected to the live site.
