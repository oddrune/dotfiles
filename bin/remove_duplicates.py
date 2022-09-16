#!/usr/bin/env python3
import sys
import hashlib
import os

all_checksums = set()

def calc_checksum(fname, block_size=2**20):
    md5 = hashlib.md5()
    f = open(fname, "rb")
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.digest()

for (dirpath, dirnames, filenames) in os.walk("."):
    for filename in filenames:
        fullpath = os.path.join(dirpath, filename) 
   
        checksum = calc_checksum(fullpath)
        if checksum in all_checksums:
            print("deleting:", fullpath)
            os.unlink(fullpath)
            continue

        all_checksums.add(checksum) 
 
