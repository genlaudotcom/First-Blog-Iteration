import rss from '@astrojs/rss';
import { SITE } from '@/data/site';
import { getPublishedPosts, slugFromId } from '@/lib/posts';

export async function GET(context) {
  const posts = await getPublishedPosts();

  return rss({
    title: SITE.title,
    description: SITE.description,
    site: context.site,
    items: posts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      link: `/blog/${slugFromId(post.id)}/`,
      categories: post.data.tags
    }))
  });
}
