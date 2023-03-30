#!/usr/bin/bash
# This script takes a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -I "$1" | grep "Content-Length:" | cut -d " " -f2
