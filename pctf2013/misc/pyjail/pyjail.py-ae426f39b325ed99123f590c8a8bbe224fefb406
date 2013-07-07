#!/usr/bin/python -u
'''
This challenge is a tribute to 'python jail' and 'The Sandboxed Terminal'
from Hack.lu 2012's CTF by Fluxfingers. Oh python, why you so why you so.
 
You should read some writeups on these (e.g. at ctftime.org/task/124/ and
ctftime.org/task/130/). You'll want to use a similar strategies to both
get past the character restrictions (e.g. `x`==repr(x) and True+True==2)
and to get past the sandboxing (e.g. the except handler below)
'''

from sys import modules
modules.clear()
del modules

_raw_input = raw_input
_eval = eval
ident = ''.join((chr(i) for i in xrange(256)))

#TIL: the interactive interpreter freaks if 'True' gets undefined,
#and 'None' is actually a keyword pretending to be a variable.
__builtins__.__dict__.clear()
__builtins__ = None

print 'Get a shell. The flag is NOT in ./key, ./flag, etc.'

while 1:
  try:
    inp = _raw_input()
    if not inp: continue
    inp = inp.split()[0][:1900]
    #Dick move: you also have to only use the characters that my solution did.
    inp = inp.translate(ident, '!"#$&*+-/0123456789;=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\^abcdefghijklmnopqrstuvwxyz|')
    a = None
    exec 'a=' + _eval(inp, {}) in {}
    print 'Return Value:', a
  except ().__class__.__bases__[0].__subclasses__()[42].__subclasses__()[0], e: #42 is base exception.
    if e.__str__().startswith('EOF'): raise e
    else: print 'Exception:', e
