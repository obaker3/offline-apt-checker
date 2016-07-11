import urllib.request
import shutil
import gzip
import glob
import os.path
# Download the file from `url` and save it locally under `file_name`:
with urllib.request.urlopen("http://gb.archive.ubuntu.com/ubuntu/dists/xenial/main/binary-amd64/Packages.gz") as response, open("/home/oliver/Desktop/package.gz", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
inF = gzip.open("/home/oliver/Desktop/package.gz", 'rb')
outF = open("/home/oliver/Desktop/package.txt", 'wb')
outF.write( inF.read() )
inF.close()
outF.close()
install = input("What package would you like to install?\n")
f = open('/home/oliver/Desktop/package.txt', 'r')

