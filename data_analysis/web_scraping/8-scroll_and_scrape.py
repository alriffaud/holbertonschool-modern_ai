#!/usr/bin/env python3
"""
Scrolls through a JS-rendered infinite-scroll product page using Selenium.
Extracts unique products with title, price, description, and rating.
"""
import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """
    Opens an infinite-scroll e-commerce page and extracts all products.
    Args:
        url (str): The URL of the infinite-scroll product page.
        scroll_pause (float): Seconds to wait between scrolls.
    Returns:
        list: A list of unique product dictionaries with keys:
              'title', 'price', 'description', and 'rating'.
    """
    # Setup headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Scroll until no new content loads
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Extract product data
    products = driver.find_elements(webdriver.common.by.By.CLASS_NAME,
                                    "thumbnail")
    seen = set()
    results = []

    for p in products:
        try:
            title = p.find_element(webdriver.common.by.By.CLASS_NAME,
                                   "title").get_attribute("title")
            price = p.find_element(webdriver.common.by.By.CLASS_NAME,
                                   "price").text
            description = p.find_element(webdriver.common.by.By.CLASS_NAME,
                                         "description").text
            stars = p.find_elements(webdriver.common.by.By.CSS_SELECTOR,
                                    ".ratings .ws-icon.ws-icon-star")

            # Avoid duplicates
            if (title, price) not in seen:
                seen.add((title, price))
                results.append({
                    "title": title,
                    "price": price,
                    "description": description,
                    "rating": len(stars)
                })
        except Exception:
            continue

    driver.quit()
    return results
