#!/usr/bin/python
import subprocess
import string
import sys
import time
import re
import socket

sHowVer = subprocess.Popen(["/usr/bin/FastCli", "-c", "show version"], stdout=subprocess.PIPE)
for line in iter(sHowVer.stdout.readline, ''):
    if 'System MAC address:' in line:
       cliCmd = "copy tftp://192.168.100.2/lab/" + line.split()[3].replace(".","").upper() + "/" + socket.gethostname().upper() + ".conf" + " flash:startup-config"
       try:
          subprocess.check_output(['Cli', '-p15', '-c' , cliCmd ])
       except subprocess.CalledProcessError as e:
          print e.output

cliCmd2 = "copy tftp://192.168.100.2/lab/firmware/arista/vEOS-lab-1.1.swi flash:vEOS-lab-1.1.swi"
try:
  subprocess.check_output(['Cli', '-p15', '-c' , cliCmd2 ])
except subprocess.CalledProcessError as e:
  print e.output

#time.sleep(10)

#cliCmd3 = "\n config terminal \n boot system flash:vEOS-lab-1.1.swi \n"
#try:
#  subprocess.check_output(['Cli', '-p15', '-c' , cliCmd3 ])
#except subprocess.CalledProcessError as e:
#  print e.output

