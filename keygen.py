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
    for i in range(2, lim):
        if gcd(i, comp) == 1:
            return i
    return None

################################################

def multinv(e, phi):
    for i in range(1, phi):
        if((e*i) % phi == 1):
            return i
    return None

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

    one = int(n).bit_length() 
    two = n
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

