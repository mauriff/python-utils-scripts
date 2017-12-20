#!/usr/bin/env python
import os, sys

print("parsing file: "+sys.argv[1] )
f = open(sys.argv[1],"r+")
f2 = open(sys.argv[1] + "_curated","w+")
d = f.readlines()
f.seek(0)
for i in d:
    if "ERROR" in i: 
        f2.write(i)
        print(i)
f2.truncate()
f2.close()
f.close()

