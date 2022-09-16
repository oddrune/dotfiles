#!/usr/bin/env python3
import sys, os

for fname in sys.argv[1:]:
  os.rename(fname, fname.lower())
