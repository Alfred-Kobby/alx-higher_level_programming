#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
    Usage: ./7-error_code.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    my_req = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(my_req.status_code))
    else:
        print(my_req.text)
