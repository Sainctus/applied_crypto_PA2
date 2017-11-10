#!/usr/bin/env python
import argparse
import sys
import os
import random
import string
import binascii



def main(keyFile, inFile, outFile):
    f = open(keyFile, 'r')
    nSize = string.rstrip(f.readline(), "\n")
    print nSize
#    nSize = binascii.unhexlify(nSize)
#    print nSize
    n = string.rstrip(f.readline(), "\n")
    print n
#    n = binascii.unhexlify(n)
#    print n
    e = string.rstrip(f.readline(), "\n")
    print e
#    e = binascii.unhexlify(e)
#    print e
    f.close()

    r = random.getrandbits(int(nSize)/2)
    for i in range(r):
        if i == "0":
            r = random.getrandbits(int(nSize)/2)

    print r


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", help="Key file", required=True)
    parser.add_argument("--i", help="Input file", required=True)
    parser.add_argument("--o", help="Output file", required=True)
    args = parser.parse_args()

    main(args.k, args.i, args.o)
