import os
import sys
import time
from SCPConnection import SCPConnection

port = 22
base_dir = "/vagrant/NetAutomation/Ansible/LAB/ConfigRepos/"

#username = sys.argv[1]
#hostname = sys.argv[2]
#password = sys.argv[3]
username = 'root'
hostname = 'server-mgmt'
password = 'admin'
#src = sys.argv[4]
#dst = sys.argv[5]
src = 'ConfigRepos/eos/LEAF01/LEAF01.conf'
dst = '/var/lib/tftpboot/lab/LEAF01.conf'

sys.stdout = open(base_dir + "LOGS/" + hostname + ".log",'a')
print "############################ STARTUP CONFIG FILE COPYING #############################"
print "Date and Time : " + time.strftime("%x") + " " + time.strftime("%X")
print "Downloaded by : " +  username
print "      File Copying        "
print "\n"
print src + '>> >>> >>' + dst

sshcon = SCPConnection(hostname, username, password)
sshcon.put(src, dst)
sshcon.close()

