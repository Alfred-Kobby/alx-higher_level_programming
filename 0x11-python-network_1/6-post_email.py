#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
    Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    my_req = requests.post(url, data=value)
    print(my_req.text)
