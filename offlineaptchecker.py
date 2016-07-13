#!/usr/bin/env python3
import urllib.request
import shutil
import gzip
import glob
import os.path
import string
packs = dict()
def convertPackagesToDict(url):
  with urllib.request.urlopen(url) as response, open("package.gz", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
  pkgfile = gzip.open("package.gz", 'rb')
  pkg=None
  depends=None
  for line in pkgfile:
    line=line.decode('utf-8').rstrip()
    if line.startswith(('Package:')):
      pkg = line[9:]
    elif line.startswith(('Depends:')):
       depends = line[9:]
    elif line == "":
       if pkg != None:
         packs[pkg] = depends
    else:
    	pass 
  return packs

if __name__ == "__main__":
  convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/main/binary-amd64/Packages.gz")
  #convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/multiverse/binary-amd64/Packages.gz")
  #convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/restricted/binary-amd64/Packages.gz")
  #convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/universe/binary-amd64/Packages.gz")
  install = input("What package would you like to install?\n")
  dependencies = packs[install]
  print("You need to install " + dependencies)
