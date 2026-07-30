#!/usr/bin/env python3
"""Generate sitemap.xml and robots.txt from the built pages.

Kyle Roof's crawl-frequency point depends on Google being able to find
every page in the first place. Priorities reflect the internal linking
pyramid: homepage top, then location and money pages, then support.
"""
import pathlib, datetime, sys

SITE = "https://jag160digital.github.io/evo-golf-website"
today = datetime.date.today().isoformat() if "--today" not in sys.argv else sys.argv[-1]

PRIORITY = {
    "index.html": ("1.0", "weekly"),
    "1-1-lessons.html": ("0.9", "monthly"),
    "beginner-coaching.html": ("0.9", "monthly"),
    "trackman-range.html": ("0.9", "monthly"),
    "trackman-simulator.html": ("0.9", "monthly"),
    "contact.html": ("0.9", "monthly"),
    "privacy.html": ("0.2", "yearly"),
    "terms.html": ("0.2", "yearly"),
}
def rank(name):
    if name in PRIORITY: return PRIORITY[name]
    if name.startswith("golf-lessons-"): return ("0.9", "monthly")   # local landing pages
    return ("0.7", "monthly")

pages = sorted(p.name for p in pathlib.Path(".").glob("*.html"))
urls = []
for n in pages:
    pr, cf = rank(n)
    loc = f"{SITE}/" if n == "index.html" else f"{SITE}/{n}"
    urls.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n"
                f"    <changefreq>{cf}</changefreq>\n    <priority>{pr}</priority>\n  </url>")

pathlib.Path("sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(urls) + "\n</urlset>\n")

pathlib.Path("robots.txt").write_text(
    f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")

print(f"sitemap.xml: {len(pages)} urls | robots.txt written")
