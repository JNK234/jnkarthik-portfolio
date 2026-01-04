#!/usr/bin/env python3
# ABOUTME: Fetches RSS feeds from Medium and Substack
# ABOUTME: Generates Hugo page bundles in content/posts/external/

import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.error import URLError
import re
import os

FEEDS = {
    "medium": "https://medium.com/@narasimhakarthik/feed",
    "substack": "https://neuraforge.substack.com/feed"
}

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "posts", "external")

# User agent to avoid 403 errors
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}


def fetch_feed(url):
    """Fetch and parse RSS feed from URL."""
    try:
        req = Request(url, headers=HEADERS)
        with urlopen(req, timeout=30) as response:
            content = response.read()
            return ET.fromstring(content)
    except (URLError, ET.ParseError) as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_date(date_str):
    """Parse RSS date string to YYYY-MM-DD format."""
    if not date_str:
        return ""
    formats = [
        "%a, %d %b %Y %H:%M:%S %Z",
        "%a, %d %b %Y %H:%M:%S GMT",
        "%a, %d %b %Y %H:%M:%S %z",
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return ""


def clean_cdata(text):
    """Remove CDATA wrapper from text."""
    if not text:
        return ""
    if "<![CDATA[" in text:
        return text.replace("<![CDATA[", "").replace("]]>", "")
    return text


def create_bundle_name(title, date):
    """Create a safe directory name from title and date."""
    # Remove special characters and convert to lowercase
    safe_title = re.sub(r'[^a-zA-Z0-9\s-]', '', title)
    safe_title = re.sub(r'\s+', '-', safe_title).lower().strip('-')
    return f"{date}-{safe_title}"


def write_content_file(post, bundle_name):
    """Write a Hugo page bundle with index.md."""
    bundle_dir = os.path.join(OUTPUT_DIR, bundle_name)
    filepath = os.path.join(bundle_dir, "index.md")
    os.makedirs(bundle_dir, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"title: \"{post['title']}\"\n")
        f.write(f"date: {post['date']}\n")
        f.write(f"externalUrl: \"{post['url']}\"\n")
        f.write(f"summary: \"Originally published on {post['source']}\"\n")
        f.write(f"source: \"{post['source']}\"\n")
        f.write(f"showReadingTime: false\n")
        f.write("---\n\n")
        f.write(f"*Originally published on {post['source']}.*\n\n")
        f.write(f"[Read the full article →]({post['url']})\n")


def parse_feed(root, source_name):
    """Parse RSS feed and extract posts."""
    posts = []
    if root is None:
        return posts

    for item in root.findall(".//item"):
        title_el = item.find("title")
        link_el = item.find("link")
        pub_date_el = item.find("pubDate")

        if title_el is not None and link_el is not None:
            title = clean_cdata(title_el.text or "")
            date_str = parse_date(pub_date_el.text if pub_date_el is not None else "")

            posts.append({
                "title": title,
                "url": link_el.text,
                "date": date_str,
                "source": source_name
            })

    return posts


def main():
    """Main function to fetch feeds and generate Hugo page bundles."""
    print("Fetching RSS feeds...")

    medium_root = fetch_feed(FEEDS["medium"])
    substack_root = fetch_feed(FEEDS["substack"])

    medium_posts = parse_feed(medium_root, "Medium")
    substack_posts = parse_feed(substack_root, "NeuraForge")

    print(f"Found {len(medium_posts)} Medium posts")
    print(f"Found {len(substack_posts)} Substack posts")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate page bundles for Medium posts
    for post in medium_posts:
        bundle_name = create_bundle_name(post['title'], post['date'])
        write_content_file(post, bundle_name)
        print(f"Created: {bundle_name}/")

    # Generate page bundles for Substack posts
    for post in substack_posts:
        bundle_name = create_bundle_name(post['title'], post['date'])
        write_content_file(post, bundle_name)
        print(f"Created: {bundle_name}/")

    total = len(medium_posts) + len(substack_posts)
    print(f"\nGenerated {total} Hugo page bundles in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
