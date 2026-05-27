# genlau.com

A modern Astro blog for `genlau.com`, built with Markdown/MDX content collections, RSS, sitemap support, responsive layouts, and Cloudflare Pages deployment settings.

## Commands

```sh
npm install
npm run dev
npm run build
npm run preview
```

## Add a Post

Create a new `.md` or `.mdx` file in `src/content/blog/`.

```md
---
title: "Post title"
description: "Short summary for cards, SEO, and RSS."
pubDate: 2026-05-27
category: "Essays"
tags: ["writing", "systems"]
featured: true
draft: false
---

Your post content here.
```

## Deploy to Cloudflare Pages

Use these Cloudflare Pages settings:

- Build command: `npm run build`
- Build output directory: `dist`
- Node.js version: `22` or newer

The included `wrangler.toml` also supports deployment with Wrangler after installing dependencies:

```sh
npx wrangler pages deploy dist --project-name genlau-blog
```
