#!/usr/bin/python3
"""
This python script takes in a URL, sends a request to
the URL and displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    if len(argv) == 2:
        r = requests.get(argv[1])
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print(r.text)
