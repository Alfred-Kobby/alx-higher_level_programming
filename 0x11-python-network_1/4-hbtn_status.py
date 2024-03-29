#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
from requests import get


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    bytes_content = response.text
    stringRes = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(bytes_content), bytes_content)
    print(stringRes)
