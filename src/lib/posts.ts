import { getCollection } from 'astro:content';

export function slugFromId(id: string) {
  return id.replace(/\.(md|mdx)$/, '');
}

export function slugify(value: string) {
  return value
    .toLowerCase()
    .trim()
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

export function resolveImagePath(image?: string) {
  if (!image) return '/social-card.svg';
  if (image.startsWith('/') || image.startsWith('http://') || image.startsWith('https://')) {
    return image;
  }

  return `/images/${image}`;
}

export function formatDate(date: Date) {
  return new Intl.DateTimeFormat('en', {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    timeZone: 'UTC'
  }).format(date);
}

export async function getPublishedPosts() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

export async function getFeaturedPosts() {
  const posts = await getPublishedPosts();
  return posts.filter((post) => post.data.featured).slice(0, 3);
}

export async function getAllTags() {
  const posts = await getPublishedPosts();
  const tags = new Map<string, number>();

  for (const post of posts) {
    for (const tag of post.data.tags) {
      tags.set(tag, (tags.get(tag) ?? 0) + 1);
    }
  }

  return [...tags.entries()]
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => a.name.localeCompare(b.name));
}

export async function getAllCategories() {
  const posts = await getPublishedPosts();
  const categories = new Map<string, number>();

  for (const post of posts) {
    categories.set(post.data.category, (categories.get(post.data.category) ?? 0) + 1);
  }

  return [...categories.entries()]
    .map(([name, count]) => ({ name, count }))
    .sort((a, b) => a.name.localeCompare(b.name));
}
