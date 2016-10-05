#! /bin/python3

# usage: python3 main.py file-with-addresses timeout

import webbrowser
import sys
import time

inputfile = sys.argv[1]
timeout = int(sys.argv[2])

baseurl = "https://maps.google.com/?t=k&q={}"

for address in open(inputfile):
    address = address.strip()
#    query = str(address.encode("punycode"))
    url = baseurl.format(address)
    print("now looking up: " + address)
    webbrowser.open(url)
    time.sleep(timeout)
