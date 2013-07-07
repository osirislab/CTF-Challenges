#!/usr/bin/python -u

import sys
from hashlib import md5
from random import choice, seed

FLAG = ''
PREFIX_LEN = 13
NEED_TO_SOLVE = 20

with open('./home/proveit/prefixes') as f:
    PREFIXES = f.readlines()

print "Free Key Distribution Service"
print "Welcome! I am more than happy to give you a key, but you must first prove you did some work!\n"

seed()

correct = 0

for _ in xrange(NEED_TO_SOLVE):
    prefix = choice(PREFIXES)[0:PREFIX_LEN]
    print "MD5 Prefix: " + prefix
    print "Enter string: ",
    data = sys.stdin.readline().rstrip().lstrip()

    if md5(data).hexdigest()[0:PREFIX_LEN] == prefix[0:PREFIX_LEN]:
        correct += 1
        print "Correct! -- Only {0} to go!".format(NEED_TO_SOLVE - correct)
    else:
        print "Wrong! :\\"
        break

if correct == NEED_TO_SOLVE:
    print "FLAG: " + FLAG
