---
title: "A Folder Structure for Future Mischief"
description: "How the blog is organized so essays, experiments, and Codex builds stay easy to add."
pubDate: 2026-05-06
category: "Codex"
tags: ["astro", "workflow", "codex"]
featured: true
draft: false
---

The main rule is simple: content belongs in `src/content/blog`, and presentation belongs in layouts and components. That keeps the site friendly to future essays, quick notes, generated prototypes, and anything else worth pinning to the wall.

## Content

Each post is a Markdown or MDX file with frontmatter for title, description, date, category, tags, and feature status. Drafts can stay in the folder with `draft: true` until they are ready.

## Pages

Astro routes live in `src/pages`. The blog index, post pages, RSS endpoint, tag pages, and category pages are all generated from the same content collection.

## Styling

Global styles live in `src/styles/global.css`. The design aims to feel sharp and internet-native without making every post compete with the interface around it.
