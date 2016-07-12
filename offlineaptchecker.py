#!/usr/bin/env python3
import urllib.request
import shutil
import gzip
import glob
import os.path
import re

## Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/main/binary-amd64/Packages.gz") as response, open("package.gz", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
inF = gzip.open("package.gz", 'rb')
outF = open("package.txt", 'wb')
outF.write( inF.read() )
inF.close()
outF.close()
packages = open('package.txt', "r" )
install = input("What package would you like to install?\n")
if install.lower() in open('package.txt').read():
    print ("This package is in the default Ubuntu repositories.\nThe program will now continue.")
else:
	print ("This package isn't in the default Ubuntu repositories.\nThe program will now quit.")
