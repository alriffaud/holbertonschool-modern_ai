#!/usr/bin/env python3
"""
Logs in to the site and scrapes quotes visible only after authentication.
"""
import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """
    Logs in to the site and scrapes quotes visible only after authentication.
    Args:
        login_url (str): The URL of the login page.
        user (str): The username.
        pwd (str): The password.
    Returns:
        list: A list of dictionaries, each containing "text", "author", and
        "tags".
    """

    # Persistent login
    session = requests.Session()

    # Get the login page to extract the CSRF token
    login_page = session.get(login_url)
    if login_page.status_code != 200:
        raise Exception("Failed to load login page")

    soup = BeautifulSoup(login_page.text, "html.parser")
    token_input = soup.find("input", {"name": "csrf_token"})
    if token_input is None or not token_input.get("value"):
        raise Exception("'NoneType' object is not subscriptable")

    csrf_token = token_input.get("value")

    # Send POST with credentials + CSRF token
    payload = {
        "csrf_token": csrf_token,
        "username": user,
        "password": pwd
    }
    response = session.post(login_url, data=payload)
    if response.status_code != 200:
        raise Exception("Login failed")

    # Get the protected page (home or quotes)
    home = session.get("https://quotes.toscrape.com/")
    if home.status_code != 200:
        raise Exception("Failed to access protected page")

    # Parser las quotes with BeautifulSoup
    soup = BeautifulSoup(home.text, "html.parser")
    quotes_data = []
    for q in soup.find_all("div", class_="quote"):
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.find_all("a", class_="tag")]
        quotes_data.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes_data
