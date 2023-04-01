#!/usr/bin/python3
"""
This script takes a URL, sends a request to that URL and displays
the value of the variable X-Request-Id in the response header.
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        url = argv[1]
        r = requests.get(url)
        print(r.headers.get('X-Request-Id'))
