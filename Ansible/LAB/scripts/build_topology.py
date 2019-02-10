#!/bin/python
import json
import jsonrpclib
from jsonrpclib import Server
import time
from pprint import pprint
import sys
import yaml
import os
import pyeapi

##########################
# CONFIGURATION OF ACCESS
##########################
username = "admin"
password = "admin"
port = 443

def connect(host,username,password,port):

  try:

    deviceCon = pyeapi.connect(transport="https", host=host, username=username, password=password, port=None)

    #print("Connecting... " + host)

    sys.stdout = open("/vagrant/NetAutomation/Ansible/LAB/ConfigRepos/LOGS/" + host + "_topology.log",'a')
    print "############################ Show LLDP Neighbors #############################"
    print "Date and Time : " + time.strftime("%x") + " " + time.strftime("%X")
    print "Checked by : " +  username
    print "\n"
    
  except pyeapi.eapilib.ConnectionError:
        errors[host] = "ConnectionError: unable to connect to eAPI"

  except pyeapi.eapilib.CommandError:
        errors[host] = "CommandError: Check your EOS command syntax"

  return deviceCon

################################
# Returns RAW python Dictionary
# with Neighbor NETCONF details
#################################


if __name__ == "__main__":

  #This will be the primary result neighborships dictionary
  neighborships = dict()

  #This will be the primary result interfaces dictionary
  interfaces = dict()

  with open(os.path.join(os.path.dirname(__file__),"lab_devices.txt"), "r") as myfile:

    devices=myfile.readlines()
    #print("DEBUG: DEVICES LOADED:")

    for line in devices:
      hostname = line.replace('\n','')
      #print hostname
      print connect(hostname,username,password,port).execute(["show hostname"])
