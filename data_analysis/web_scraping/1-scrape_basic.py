#!/usr/bin/env python3
"""
Scrapes the first page of quotes from quotes.toscrape.com
using requests and BeautifulSoup.
"""
from bs4 import BeautifulSoup
fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """
    Scrape the first page of quotes from the given URL.
    Args:
        url (str): The URL of the Quotes to Scrape page.
    Returns:
        list: A list of dictionaries with keys "text", "author", and "tags".
    """
    # Fetch the HTML content using the helper function
    html = fetch_html(url)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all quote blocks
    quote_blocks = soup.find_all("div", class_="quote")

    quotes_data = []

    # Iterate through each quote block
    for block in quote_blocks:
        # Extract quote text
        text = block.find("span", class_="text").get_text(strip=True)
        # Extract author name
        author = block.find("small", class_="author").get_text(strip=True)
        # Extract tags (list of strings)
        tags = [tag.get_text(strip=True)
                for tag in block.find_all("a", class_="tag")]

        # Append the data as a dictionary
        quotes_data.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes_data
