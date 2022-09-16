#!/usr/bin/env python3
import os, glob, sys

old_ch = sys.argv[1]
new_ch = sys.argv[2]

for oldname in glob.glob("*"):
    newname = oldname.replace(old_ch, new_ch)
    if newname != oldname:
        os.rename(oldname, newname)
