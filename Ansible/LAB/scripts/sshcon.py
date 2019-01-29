#!/usr/bin/env pythdon

# Author: Priyan Ariyasinghe
# Date: Dec 30  2016
# Author: Priyan Ariyasinghe
# Date: Dec 30  2016
# Description: This script can be used as import libraryi, making SSH2 connections using Paramiko,
#              allows network-admins to login to network devices programmatically and execute of commands.
# Supported devices: Linux, Arista, Brocade, Cisco and Fortinet

import paramiko
import time
import socket
import yaml

class sshcon:
      _hostname = None
      _username = None
      _password = None
      _en_password = None
      _host_Conn = None
      _remote_Conn = None

      def __init__(self, hostname, username, password, en_password):

          self._hostname = hostname
          self._username = username
  	  self._password = password
          self._en_password = en_password   

      def _open(self):
  
   	  #remote_Conn = None
 
   	  try:

      		self._remote_Conn = paramiko.SSHClient()
      		self._remote_Conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      		self._remote_Conn.connect(self._hostname,username=self._username,password=self._password, look_for_keys=False, allow_agent=False)

      		print "SSH connection established to %s" % self._hostname

      		self._host_Conn = self._remote_Conn.invoke_shell()
      		print "Interactive SSH session established"
      		output_Conn = self._host_Conn.recv(1000)
      		print output_Conn
      		time.sleep(1)

      		if '#' not in output_Conn:
          	   self._host_Conn.send('en\n')
          	   time.sleep(1)
                   print '\t*** Sending Enabling Password **** '
                   self._host_Conn.send(self._en_password)
                   self._host_Conn.send('\n')
                   time.sleep(1)
                   output_Conn = self._host_Conn.recv(1000)

      		if '#' in output_Conn:
          	   print '\t*** Your In Enabled Mode **** '
          	   #host_Conn.send('terminal lenght 0\n')
          	   time.sleep(1)

      		else:
          	   print '\t*** Incorrect Enabed Password ***'

   	  except paramiko.SSHException:
           	  print '\t*** Probably Your Not Authorised To Acceess ***'

   	  except socket.error:
           	  print 't\*** s% is Unreachable ***' % self._hostname


      def _close(self):

	  if self._remote_Conn:
             self._host_Conn.close()
             self._remote_Conn.close()


      def host_COMMAND(self,cmd):
    	  '''*** Command ***'''

          self._open()

    	  self._host_Conn.send("\n")

    	  self._host_Conn.send(cmd + "\n")

       	  time.sleep(2)

    	  output_Conn = self._host_Conn.recv(5000)

          self._close()

    	  return output_Conn

      def host_COMMANDS_YAML(self,cmds):
          '''*** Commands ***'''

          self._open()

          file = open(cmds,'r')
       
          with open(cmds,"r") as file:
               commands = yaml.load(file)

          for line in commands:
          
              self._host_Conn.send("\n")

              self._host_Conn.send(line + "\n")

              time.sleep(1)

              output_Conn = self._host_Conn.recv(500)
              
              print output_Conn

          self._close()


      def host_COMMANDS(self,cmds):
          '''*** Commands ***'''

          self._open()

          with open(cmds,"r") as file:

            for line in file.readlines():

                line = line.strip()

                self._host_Conn.send("\n")

                self._host_Conn.send(line + "\n")

                time.sleep(1)

                output_Conn = self._host_Conn.recv(500)

                print output_Conn

          file.close()

          self._close()

