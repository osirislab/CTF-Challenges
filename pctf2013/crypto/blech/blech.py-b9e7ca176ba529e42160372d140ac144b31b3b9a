#!/usr/bin/python -u
import sys
import struct
import os
import hashlib

def strtonum(s):
  ret = 0
  for h in s:
    ret *= 256
    ret |= ord(h)
  return ret

def numtostr(s, l):
  ret = ""
  for i in range(0, l):
    ret = chr(s&0xFF) + ret
    s >>= 8
  return ret

port = 1234

# RSA modulus(factor me)
N = 0xc3542f8b7b2c9f083912972d8d07312fce5cf549ae8b25e97a691d35a72f953dad939811e1ec4d46fafd5db3034fee45c5f700a57915a67238925361b3ea7ae58e392b92d13af8e1604298794f640db466642933825813bf329b228f773a5137a625bd23ffa1d8bb7ca9b49d6235a0e4f839226f14a9e7a42fa4f7d530725803

print "WE ONLY RUN SIGNED CODE, DO YOU HAVE SIGNED CODE?"
l = struct.unpack("I", sys.stdin.read(4))[0]
hashee = sys.stdin.read(0x80)
msg = numtostr(pow(strtonum(hashee), 3, N), 0x80)
code = sys.stdin.read(l)
if msg[0:4] != "\x00\x01\xFF\xFF":
  print "BAD PADDING"
  sys.exit(0)
h = hashlib.sha1(code).digest()
if msg[len(msg)-len(h):] != h:
  print "BAD HASH"
  sys.exit(0)
eval(code)
