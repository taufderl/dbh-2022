#!/usr/bin/env python3

import IPython
from pwn import *

r = remote('20.126.227.19', 45377)
resp = ""
# sum
while not 'ieviel' in str(resp):
    resp = r.recvline()
    print(resp)
s = str(resp).split('"')[1]
s = s.split('+')
s = int(s[0]) + int(s[1])
r.sendline(str(s))
# normalize
while not 'Normalisieren' in str(resp):
    resp = r.recvline()
    print(resp)
s = resp.split(b' ')[-2][:-1]
s = s.replace(b'-', b'')
print(s)
r.sendline(s)
# ROT13
while not 'ROT13' in str(resp):
    resp = r.recvline()
    print(resp)
s = str(resp).split(' ')[-2][:-1]
rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
s = bytes(str(s).translate(rot13), 'ascii')
print(s)
r.sendline(s)
# base64
while not 'Base64-enkodierten' in str(resp):
    resp = r.recvline()
    print(resp)
s = resp.split(b' ')[-2][:-1]
import base64
s = base64.b64decode(s)
r.sendline(s)
# hex
while not 'hexadezimal-enkodierten' in str(resp):
    resp = r.recvline()
    print(resp)
s = resp.split(b' ')[-2][:-1]
print(s)
print(s.decode('ascii'))
s = binascii.a2b_hex("%s" % (s.decode('ascii')[2:].strip())).decode("ASCII").replace(';', '\n- ')
print(s)
r.sendline(s)
#bin2dec
while not '(dezimal)' in str(resp):
    resp = r.recvline()
    print(resp)
s = resp.split(b' ')[-2][:-1]
binary = s.decode('ascii')
s = int(binary, 2)
r.sendline(str(s))
#bin2dec
while not 'VerXORe' in str(resp):
    resp = r.recvline()
    print(resp)
v1 = resp.split(b' ')[-1][:-2].decode('ascii')
v2 = resp.split(b' ')[1].decode('ascii')
print(v1, v2)
s = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(v1, v2)])
print(s)
r.sendline(str(s))
#Schirmherrin
while not 'Schirmherrin' in str(resp):
    resp = r.recvline()
    print(resp)
r.sendline('Judith Gerlach')
while not 'DBH{' in str(resp):
    resp = r.recvline()
    print(resp)
IPython.embed()
#r.interactive()
