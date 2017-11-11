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
    d = string.rstrip(f.readline(), "\n")
    d = int(d)
    f.close()

    ###########################################
    #Read cipher from file#
    
    f = open(inFile, 'r')
    m = string.rstrip(f.readline(), "\n")
    f.close()
    print m

    ###########################################
    #Conver to int and decrypt
    
    m = int(m)

    final = pow(m, d, n)

    ###########################################
    #Cut out randomness#
    
    final = str(final)
    print final

    i = final.find("0")

    final = final[i:]

    print final

    ###########################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", help="Key file", required=True)
    parser.add_argument("--i", help="Input file", required=True)
    parser.add_argument("--o", help="Output file", required=True)
    args = parser.parse_args()

    main(args.k, args.i, args.o)
