#!/usr/bin/env python

from sshcon import sshcon
from os.path import expanduser
import sys
import yaml
import time

base_dir = expanduser("~/ansible/CFG/HPN/REPOS/LAB")
hostname = sys.argv[1]
command_file = sys.argv[2]
username = sys.argv[3] 
password = sys.argv[4]
en_password = 'admin'

host = sshcon(hostname,username,password,en_password)

sys.stdout = open(base_dir + "/LOG/" + hostname + ".log",'a')

print "############################ CHANGES #############################"
print "Date and Time : " + time.strftime("%x") + " " + time.strftime("%X")  
print "Changes made by : " +  username
print "\n"
host.host_COMMANDS(base_dir + "/CHANGES/" + hostname + "/" + command_file)
print "\n"

