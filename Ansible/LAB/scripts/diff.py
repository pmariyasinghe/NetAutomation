#!/usr/bin/env python
import sys
import difflib
#from difflib_data import *

# Ask the user to enter the names of files to compare
file1 = sys.argv[1]
file2 = sys.argv[2] 

def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())


    with open(File2,'r') as f:
        e=set(f.readlines())

    File3 = '/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/CHANGES/TORCHB/2017-09-13-base-diff.conf'

    open(File3,'w').close() #Create the file

    with open(File3,'a') as f:
         diff = difflib.ndiff(d,e)
         f.write('\n'.join(list(diff)))

compare(file1,file2)
