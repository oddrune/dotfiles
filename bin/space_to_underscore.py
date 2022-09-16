#!/usr/bin/env python3
import os, glob, sys

try:
  replace_char = sys.argv[1]
  assert len(replace_char) == 1
except:
  replace_char = "_"

for oldname in glob.glob("*"):
    newname = oldname.replace(" ", replace_char)
    if newname != oldname:
        os.rename(oldname, newname)
