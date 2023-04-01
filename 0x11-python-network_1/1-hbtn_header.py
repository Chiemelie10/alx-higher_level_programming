#!/usr/bin/python3
"""
This script takes in a URL, sends a request to that URL and
displays the value of the "X-Request-Id" variable found in the
header of the response.
"""

if __name__ == '__main__':
    from urllib import request
    from sys import argv

    if len(argv) == 2:
        url = argv[1]
        with request.urlopen(url) as response:
            X_Request_Id = response.getheader('X-Request-Id')
            print(X_Request_Id)
