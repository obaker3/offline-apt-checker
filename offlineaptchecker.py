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
      pkg = line#!/usr/bin/env python3
import urllib.request
import shutil
import gzip
import glob
import os.path
import string
import re
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
  
def  installedPackages(txt):   
  installtemp = open(txt, 'r')#opens a text file with the complete list of installed packages.
  count = 0    
  for line in installtemp:
    count += 1
    if count > 5:
      installed=line.split()[1]
      #print (installed)

if __name__ == "__main__":
  convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/main/binary-amd64/Packages.gz")#Adds [MAIN] from the Ubuntu repo to a dictionary 
  #convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/multiverse/binary-amd64/Packages.gz")#Adds [MULTIVERSE] from the Ubuntu repo to a dictionary 
  #convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/restricted/binary-amd64/Packages.gz")#Adds [RESTRICTED] from the Ubuntu repo to a dictionary 
  #convertPackagesToDict("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/universe/binary-amd64/Packages.gz")#Adds [UNIVERSE] from the Ubuntu repo to a dictionary 
  install = input("What package would you like to install?\n")
  installedPackages('installed.txt')		
  dependencies = packs[install]#Creates the primary dependencies for the specified package
  deps=[]
  depends1 = [dependencies.strip(" ") for dependencies in dependencies.split(',')]
  for dep in dependencies:
    depends1 = [dep.split(",")]
    #dependsprimary = [depends1.split(" ")]

    #depends1=dependencies.split(",")
    deps.append(depends1 = [i.split(',')[0] for i in dependencies].lstrip())
  print (depends1)
  print (dependsprimary)

  		  

  		
  		

  
  #print("You need to install " + dependencies)#Shows what packages will need to be installed (primary only)
  #for dep in dependencies.split():##Repeats for every dependency in the package
  	
  	#exit()
#'installed.txt', 'r'
    
#print ("You must create a package called installed.txt in the current working directory with the command dpkg -l > installed.txt")
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
