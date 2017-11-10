#!/usr/bin/env python
from Crypto.Util import number
import argparse
import sys
import os
import random
import binascii

################################################

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

################################################

def gencoprime(comp, lim):
    i = 0
    while i < lim:
        if number.isPrime(i) and gcd(i, comp) == 1:
            return i
        else:
            i += 1

    return -1

################################################

def extended_gcd(a, b):
    x, lastx, y, lasty = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty

def multinv(e, phi):
    x, y = extended_gcd(e, phi)
    if x < 0:
        return phi + x
    return x
    
################################################

def main(pubFile, privFile, nBits):
    p = number.getPrime(int(nBits).bit_length())
    q = number.getPrime(int(nBits).bit_length())
    while q == p:
        q = number.getPrime(int(nBits).bit_length())

    n = p * q
    phi = (p - 1) * (q - 1)

    e = gencoprime(phi, phi)

    d = multinv(e, phi)

    one = int(nBits).bit_length() 
    two = nBits
    thr = e
    fou = d

    f = open(pubFile, 'w')
    f.write(str(one) + "\n")
    f.write(str(two) + "\n")
    f.write(str(thr) + "\n")
    f.close()

    f = open(privFile, 'w')
    f.write(str(one) + "\n")
    f.write(str(two) + "\n")
    f.write(str(fou) + "\n")
    f.close


################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", help="Public key file", required=True)
    parser.add_argument("--s", help="Private key file", required=True)
    parser.add_argument("--n", help="Number of bits in N", required=True)
    args = parser.parse_args()

    main(args.p, args.s, args.n)

