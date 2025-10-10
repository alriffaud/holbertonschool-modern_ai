#!/usr/bin/env python3
"""
Fetches the HTML content of a web page.
"""
import requests


def fetch_html(url, headers=None, timeout=10):
    """
    Sends an HTTP GET request to a given URL and returns the full HTML as a
    string. It supports custom headers (like User-Agent) and timeout control.
    Raises exceptions for all HTTP errors (status >= 400).
    Args:
        url (str): The URL of the page to retrieve.
        headers (dict, optional): Custom HTTP headers.
        timeout (int, optional): Number of seconds to wait before aborting.
        Default is 10.
    Returns:
        str: The full HTML of the response as a string.
    Raises:
        requests.exceptions.RequestException: For any network or HTTP error.
    """

    # Send the HTTP GET request
    response = requests.get(url, headers=headers, timeout=timeout)

    # Raise an exception for HTTP errors (status >= 400)
    response.raise_for_status()

    # Return the HTML content of the response
    return response.text
