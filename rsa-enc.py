#!/usr/bin/env python
import argparse
import sys
import os
import random
import string
import binascii



def main(keyFile, inFile, outFile):
    ###########################################
    #Read key info from file#
    
    f = open(keyFile, 'r')

    nBits = string.rstrip(f.readline(), "\n")
    nBits = int(nBits)
    
    n = string.rstrip(f.readline(), "\n")
    n = int(n)
    
    e = string.rstrip(f.readline(), "\n")
    e = int(e)
    
    f.close()

    ###########################################
    #Generate randomness#

    r = random.getrandbits(int(nBits/2))
    r = bytes(r)
    while 1:
        if r.find(b'0') != -1:
            r = random.getrandbits(int(nBits/2))
            r = bytes(r)
        else:
            break
    print r
    
    rand = b"0" + b"2" + r + b"0"
    print rand

    ###########################################
    #Read message from file#
    
    f = open(inFile, 'r')
    m = string.rstrip(f.readline(), "\n")
    f.close()
    print m

    ###########################################
    #Concat and encrypt#
    
    enc = rand + bytes(m)
    enc = int(enc)
    print enc

    print "enc bit length = " + str(enc.bit_length()) + "\n" 

    final = pow(enc, e, n)
    print final

    ###########################################
    #Write result to file#
    
    f = open(outFile, 'w')
    f.write(str(final))
    f.close()

    ###########################################


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", help="Key file", required=True)
    parser.add_argument("--i", help="Input file", required=True)
    parser.add_argument("--o", help="Output file", required=True)
    args = parser.parse_args()

    main(args.k, args.i, args.o)
