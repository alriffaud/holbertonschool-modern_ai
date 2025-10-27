#!/usr/bin/env python3
"""
Scrapes a single product detail page using Selenium (headless Chrome).
Extracts product title, price, description, and rating.
"""
import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """
    Opens a product detail page and returns a dictionary with:
    - title: the product title (second <h4> inside .caption)
    - price: the product's price (text of <h4 class="price">)
    - description: the full description (text of <p class="description">)
    - rating: the number of stars (.glyphicon-star elements under .ratings)
    Args:
        url (str): The URL of the static product detail page.
        delay (float): Time to wait for the page to load.
    Returns:
        dict: A dictionary containing the product details.
    """
    # Set up headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(delay)  # wait for page to load

    # Extract product details
    title = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR, ".caption h4:nth-of-type(2)"
    ).text

    price = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR, "h4.price"
    ).text

    description = driver.find_element(
        webdriver.common.by.By.CSS_SELECTOR, "p.description"
    ).text

    stars = driver.find_elements(
        webdriver.common.by.By.CSS_SELECTOR,
        ".ratings .ws-icon.ws-icon-star"
    )

    driver.quit()

    return {
        "title": title,
        "price": price,
        "description": description,
        "rating": len(stars)
    }
