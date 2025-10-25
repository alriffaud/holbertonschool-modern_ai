#!/usr/bin/env python3
"""
Extracts quotes from embedded JSON-LD blocks on a web page.
"""
import json
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """
    Extracts quotes from <script type="application/ld+json"> blocks.
    Args:
        url (str): The URL of the Quotes to Scrape page.
    Returns:
        list: A list of dictionaries, each containing "text", "author",
        and "tags".
    """
    html = fetch_html(url)
    quotes = []

    # Search JSON-LD blocks manually
    start_tag = '<script type="application/ld+json">'
    end_tag = '</script>'
    start = 0

    while True:
        start = html.find(start_tag, start)
        if start == -1:
            break
        start += len(start_tag)
        end = html.find(end_tag, start)
        if end == -1:
            break

        json_block = html[start:end].strip()

        try:
            data = json.loads(json_block)
        except json.JSONDecodeError:
            continue  # Ignore malformed blocks

        # If the block corresponds to a quote
        if isinstance(data, dict) and data.get("@type") == "Quote":
            text = data.get("text", "")
            author = data.get("author", {}).get("name", "") if isinstance(
                data.get("author"), dict) else ""
            keywords = data.get("keywords", [])
            if isinstance(keywords, str):
                tags = [tag.strip() for tag in keywords.split(",")]
            else:
                tags = keywords if isinstance(keywords, list) else []

            quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })

    return quotes
