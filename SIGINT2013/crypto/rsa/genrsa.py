#!/usr/bin/env python

from time import time
from os import system
from Crypto.PublicKey import RSA


SEED = int(time())


def randfunc(n):
    def rand():
        global SEED
        ret = SEED*0x1333370023004200babe004141414100e9a1192355de965ab8cc1239cf015a4e35 + 1
        SEED = ret
        return (ret >> 0x10) & 0x7fff
    ret = ""
    while len(ret) < n:
        ret += chr(rand() & 0xff)
    return ret


keypair = RSA.generate(1024, randfunc)


with open("pub", "w") as pubfile, open("id_rsa", "w") as privfile:
    privfile.write(keypair.exportKey())
    pubfile.write(keypair.publickey().exportKey())

system("ssh-keygen -m PKCS8 -i -f pub > id_rsa.pub && rm pub")
