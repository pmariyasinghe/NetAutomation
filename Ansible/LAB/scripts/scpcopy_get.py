import os
import sys
import time
from SCPConnection import SCPConnection
 
port = 22
#password = 'D%sec9an'
#password = 'wcranhe'

dfile = sys.argv[2].upper() + ".conf"
base_dir = "/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/LAB/"
src = "/mnt/flash/startup-config"
dpath = base_dir + "CURRENT/"
dst = dpath + dfile

username = sys.argv[1]
hostname = sys.argv[2]
password = sys.argv[3]

try:
   with open(dst, 'r') as f:
        f.close()
except IOError:
   with open(dst, 'w') as f:
        f.close()

sys.stdout = open(base_dir + "LOG/" + hostname + ".log",'a')
print "############################ STARTUP CONFIG DOWNLOAD #############################"
print "Date and Time : " + time.strftime("%x") + " " + time.strftime("%X")
print "Downloaded by : " +  username
print "      File downloading        "
print "\n"
print src + '>> >>> >>' + dst

sshcon = SCPConnection(hostname, username, password)
sshcon.get(src, dst)
sshcon.close()
