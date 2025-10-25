#!/usr/bin/env python3
"""
Scrapes all quotes from quotes.toscrape.com via its JSON API.
Uses only json and fetch_html as allowed.
"""
import json
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """
    Fetches quote data from all API pages of quotes.toscrape.com.
    Args:
        base_url (str): The root URL of the site, e.g.
        "https://quotes.toscrape.com".
    Returns:
        list: A list of dictionaries, each containing:
            - "text": the quote text
            - "author": the author's name
            - "tags": a list of tag strings
    """
    all_quotes = []
    page = 1

    while True:
        # Build endpoint URL manually (without urllib)
        if base_url.endswith('/'):
            api_url = f"{base_url}api/quotes?page={page}"
        else:
            api_url = f"{base_url}/api/quotes?page={page}"

        # Get JSON text from API
        response_text = fetch_html(api_url)

        # Convert JSON string to Python dictionary
        data = json.loads(response_text)

        # Extract citations from the current page
        for quote in data.get("quotes", []):
            all_quotes.append({
                "text": quote.get("text", "").strip(),
                "author": quote.get("author", {}).get("name", "Unknown"),
                "tags": quote.get("tags", [])
            })

        # Check if there are more pages
        if not data.get("has_next"):
            break

        page += 1

    return all_quotes
