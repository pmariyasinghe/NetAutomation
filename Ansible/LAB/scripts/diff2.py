#!/usr/bin/env python
import sys
from os.path import expanduser
import difflib
#from difflib_data import *

base_dir = expanduser("~/ansible/CFG/HPN/REPOS/CHANGES/")

# Task uses the names of files to compare and the output file
file1 = base_dir + sys.argv[1] + sys.argv[2]
file2 = base_dir + sys.argv[1] + sys.argv[3] 
fileo = base_dir + sys.argv[1] + sys.argv[4]
lineAdd = False
lineDel = False

with open(file1,'r') as f:
    flines = f.readlines()
 
with open(file2,'r') as g:
    glines = g.readlines()

#    d = difflib.Differ()
#    diff = d.compare(flines, glines)
#    print("\n".join(diff))

diff = difflib.ndiff(flines,glines)

changes = [l for l in diff if l.startswith('+ ') or l.startswith('- ')]

with open(fileo,'w') as f:
     for c in changes:
         if c.startswith('- '):
            if lineDel == False:
               lineAdd = False 
               f.write('!\n')
               lineDel = True
            f.write(c.replace('- ', 'no '))
         if c.startswith('+ '):
            if lineAdd == False:
               lineDel = False
               f.write('!\n')
               lineAdd = True
            f.write(c.replace('+ ', ''))
     f.write('!\n')
