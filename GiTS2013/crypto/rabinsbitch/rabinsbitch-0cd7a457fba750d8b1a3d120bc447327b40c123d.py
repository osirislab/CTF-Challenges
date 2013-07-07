#
#for the answer take the hash of p,q concatenated together as decimal strings
#such as if p=7,q=11 p being by definition smaller you'd hash the string "711"
#please hash with sha512, thank you and g'luck

import math
import operator
import random,struct
import os,SocketServer
import base64 as b64

def encrypt(m,n):
    c=pow(m,2,n)
    return c
def extended_gcd(a, b):
    if b == 0:
       return (1, 0)
    else:
        (q, r) = (a/b, a%b)
        (s, t) = extended_gcd(b, r)
        return (t, s - q * t)
def invmod(a, p, maxiter=1000000):
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in xrange(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

def reste_chinois(la,lm):
    """
    Return the solution of the Chinese theorem.
    """
    M = reduce(operator.mul, lm)
    lM = [M/mi for mi in lm]
    ly = map(invmod, lM, lm)
    laMy = map((lambda ai, Mi, yi : ai*Mi*yi), la, lM, ly)
    return sum(laMy) % M

def decrypt(c,p,q):
    mp=pow(c,(p+1)/4,p)
    mq=pow(c,(q+1)/4,q)
    r1 = pow(c, (p+1)/4, p)
    r2 = pow(c, (q+1)/4, q)

    return (reste_chinois([r1, r2], [p, q]), \
                reste_chinois([-r1, r2], [p, q]), \
                reste_chinois([r1, -r2], [p, q]), \
                reste_chinois([-r1, -r2], [p, q]))    
p=7
q=11
n=p*q
TEST=True
if TEST:
    m=[]
    for x in xrange(200):
        m.append(random.getrandbits(1200))
    print m[0]
    print len(set(m))
    assert(len(set(m))>2)
    i=0
    print decrypt(3,p,q)
    for x in m:
        enc=encrypt(x,n)
        if i%20==0:
            print "ENCRYPTED IS %r" %enc
        i+=1
        assert(x in decrypt(enc,p,q) )

class  SignHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        req=self.request
		req.sendall("You must first solve a puzzle, a sha1 sum ending in 26 bit's set to 1, it must be of length %s bytes, starting with %s"%(len(proof)+5,proof))
		test=req.recv(21)
		ha=hashlib.sha1()
		ha.update(test)
		if (test[0:16]!=proof or ord(ha.digest()[-1])!=0xff or 
            ord(ha.digest()[-2])!=0xff or
			ord(ha.digest()[-3])!=0xff or
			ord(ha.digest()[-4])&3!=3 
			):
			req.sendall("NOPE")
			req.close()
			return

        leng=struct.unpack("H",req.recv(2))[0]
        s=""
        while len(s)<leng:
            s+=req.recv(leng-len(s))
        if len(s)> leng:
            req.sendall("Okaly Doakaly")
            req.close()
            return
        i=0
        s=s[::-1]
        for el in xrange(len(s)):
            i+=(ord(s[el])<<(8*el))
        rets=decrypt(i,p,q)
        for el in rets[:-1]:
            req.sendall(str(el)+",")
        req.sendall(str(rets[-1]))


        req.close()


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
   pass
if __name__ == "__main__" and not TEST:
   HOST, PORT = "", 9955
   server = ThreadedServer((HOST, PORT), SignHandler)
   server.allow_reuse_address = True
   server.serve_forever()
