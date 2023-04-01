#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response decoded in utf-8.
"""

if __name__ == '__main__':
    from urllib import request, error
    from sys import argv

    if len(argv) == 2:
        url = argv[1]
        req = request.Request(url)
        try:
            with request.urlopen(req) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
