#!/usr/bin/env python3

import os, glob, sys, shutil

try:
    files_per_dir = int(sys.argv[1])
except:
    print("syntax: %s files_per_directory" % sys.argv[0])
    sys.exit(1)

all_files = list(filter(os.path.isfile, glob.glob("*")))
all_files.sort()

if files_per_dir <= 15:
  num_folders = int(files_per_dir)
  files_per_dir = (len(all_files)/num_folders)+1
else:
  num_folders = int(len(all_files) / files_per_dir) + 1
folder_base = os.path.basename(os.getcwd()) + "-"

print("Files:  ", len(all_files))
print("Folders:", num_folders)

files_per_dir = int(files_per_dir)
for fnum in range(1, num_folders+1):
    newfolder = "%s%02d" % (folder_base, fnum)
    print("Current folder:", newfolder)
    try:
      os.mkdir(newfolder)
    except: pass
    for filename in all_files[:files_per_dir]:
        shutil.move(filename, newfolder)

    all_files = all_files[files_per_dir:]

    try:
        os.rmdir(newfolder)
    except:
        pass
