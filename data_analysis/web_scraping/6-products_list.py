#!/usr/bin/env python3
"""
Scrapes a static e-commerce category page using Selenium (headless Chrome).
Extracts product title, price, description, and rating.
"""
import time
from selenium import webdriver


def scrape_products(url):
    """
    Opens a static product category page and returns a list of product
    dictionaries.
    Args:
        url (str): The URL of the static product category page.
    Returns:
        list: A list of dicts with keys 'title', 'price', 'description', and
        'rating'.
    """
    # Set up Chrome in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(1)  # ensure page loads

    products_data = []

    # Each product is inside a div with class "thumbnail"
    products = driver.find_elements(webdriver.common.by.By.CLASS_NAME,
                                    "thumbnail")

    for p in products:
        # Extract data fields
        title = p.find_element(webdriver.common.by.By.TAG_NAME,
                               "a").get_attribute("title")
        price = p.find_element(webdriver.common.by.By.CLASS_NAME,
                               "price").text
        description = p.find_element(webdriver.common.by.By.CLASS_NAME,
                                     "description").text
        rating = p.find_element(webdriver.common.by.By.CSS_SELECTOR,
                                ".ratings p[data-rating]").get_attribute(
                                    "data-rating")

        products_data.append({
            "title": title,
            "price": price,
            "description": description,
            "rating": int(rating)
        })

    driver.quit()
    return products_data
