#!/usr/bin/env python3

import requests
import string

#chars = string.printable
chars = '123456789abcdef'

def brute():
    key = ''
    index = 0
    while True:
        for c in chars:
            testkey = key + c
            burp0_url = "http://000990aa23-rev-connector.dbhchallenge.net:80/?ID=c56ac9e5a4faa7e8d694715ea6d1bff5&debug=true&key={key}".format(key=testkey)
            resp = requests.get(burp0_url)
            if 'Wrong char at position {index}'.format(index=index+1) in resp.text:
                print('Found next char: '+testkey)
                key = testkey
                index+=1
                continue
            elif 'DBH' in resp.text:
                print('[*] Found key: '+testkey)
                print(resp.text)
                return


brute()

"""
user@ubuntu:~/git/dbh-2022/rev_connector$ HTTP_PROXY=http://127.0.0.1:8080 ./brute.py 
[*] Found key: ed5423f8cc0d0927273a57e4701c2c17
DBH{cfa7e2d1-f588-47c0-adfc-7339ac29cbb1}

"""
