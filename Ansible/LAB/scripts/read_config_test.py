#!/usr/bin/env python

from os.path import expanduser
import sys
import time
import yaml

inFile = "/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/CURRENT/torche"
outFile = "/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/CURRENT/torche.yml"
ifLine = False
portConf = False

with open(inFile,"r") as ifile:

     with open(outFile,"w") as ofile:
 
          #ofile = yaml.dump(ifile) 
          print(yaml.dump(ifile))
     
#     ofile.close()

ifile.close()

