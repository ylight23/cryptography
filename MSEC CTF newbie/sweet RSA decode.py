from sympy import randprime, nextprime

from Crypto.Util.number import *

import math
from gmpy2 import iroot
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def fermat(n):
    a = isqrt(n)
    b2 = a*a - n
    b = isqrt(n)
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2)
        count += 1
    p = a+b
    q = a-b
    assert n == p * q
    return p, q


def main():
    e = 65537
    n = 0xb3f2e4f4431947de914b9600965fb3b1d9375777a9b605465658aca00df50ea5786532239ef749830e1f73ed5a51e3513708fd30d53f5cb75619f9a97ca36355066f0dde4273205e0c90f4ba1cd2582d44ec209b29d2453f532dadd3f923c2f6fd4019fce6818f6023bc43e4425eab8e2dd4d4826023d4265f191efa4aab77a7
    p, q = fermat(n)
    #print(p)
    #print(q)
    phi= (p-1)*(q-1)
    ct =  0x72e68b0490cd9bf85225432bfd6f9617550af6534755b2921e1e150d284258ac1ac39747e15f5411f9a02d37d985ad78a0763a7927cec2a997751001be996267ccfff2e35f2dddfd069bdb666f9a8b20f1da433ff7710750fe3faa8c1e00f4b7c0160c0a6bee86101ed7a03f1edb45d27a7efb8269609eb4ec810b459c3c8869 
    d= pow(e,-1,phi)

    print("phi  =", phi)
    print(long_to_bytes(pow(ct,d,n)))
if __name__ == '__main__':
    main()