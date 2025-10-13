#!/usr/bin/env python3
"""
Scrapes all quotes from quotes.toscrape.com by following pagination links.
"""
import time
from bs4 import BeautifulSoup
from urllib import parse

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """
    Follows 'Next' links on quotes.toscrape.com until no more pages remain.
    Args:
        base_url (str): The URL of the first page
        (e.g. https://quotes.toscrape.com/)
    Returns:
        list: A list of dictionaries containing all quotes with keys "text",
        "author", and "tags".
    """
    all_quotes = []
    current_url = base_url

    while True:
        # Fetch and parse the current page
        html = fetch_html(current_url)
        soup = BeautifulSoup(html, "html.parser")

        # Scrape the quotes from this page
        page_quotes = scrape_basic(current_url)
        all_quotes.extend(page_quotes)

        # Find the "Next" link
        next_li = soup.find("li", class_="next")
        if not next_li:
            break  # No more pages

        next_href = next_li.find("a")["href"]
        current_url = parse.urljoin(current_url, next_href)

        # Be polite: wait before next request
        time.sleep(1)

    return all_quotes
