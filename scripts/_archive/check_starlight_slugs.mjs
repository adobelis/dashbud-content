// Quick check — list files Starlight would see as content
import { readdir } from 'fs/promises';
import { join } from 'path';

async function walk(dir, prefix = '') {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const e of entries) {
    const rel = prefix ? `${prefix}/${e.name}` : e.name;
    if (e.isDirectory()) {
      await walk(join(dir, e.name), rel);
    } else if (e.name.endsWith('.md') || e.name.endsWith('.mdx')) {
      const slug = rel.replace(/\.mdx?$/, '').replace(/\/index$/, '');
      console.log(slug);
    }
  }
}

await walk('/Users/arthur/www/dashbud/content/wiki/src/content/docs');
