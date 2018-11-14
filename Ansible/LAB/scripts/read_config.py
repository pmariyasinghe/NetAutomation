#!/usr/bin/env python

from os.path import expanduser
import sys
import time
import yaml

def load_POlines(line):

    if 'description' in line :
        tline = ""
        for i in xrange(1,len(line.split())):
            tline = tline + " " + line.split()[i]
        return "       description: '" + tline + "' ,\n"

    elif 'access vlan' in line :
          return "       nvlan: none ,\n" + "       trunk: false ,\n" + "       vlan: " + line.split()[3] + " ,\n"

    elif 'trunk native vlan' in line :
          return  "       nvlan: '" + line.split()[4] + "' ,\n"

    elif 'trunk allowed vlan' in line :
          return  "       trunk: true ,\n" + "       vlan: '" + line.split()[4] + "' ,\n"

    else: 
          return " "

def load_Ethlines(line):

    if 'description' in line :
        tline = ""
        for i in xrange(1,len(line.split())):
            tline = tline + " " + line.split()[i]
        return "       description: '" + tline + "' ,\n"

    elif 'channel-group' in line :
          return  "       channel_group: '" + line.split()[1] + "' ,\n"

    elif 'access vlan' in line :
          return "       nvlan: none ,\n" + "       trunk: false ,\n" + "       vlan: " + line.split()[3] + " ,\n"

    elif 'trunk native vlan' in line :
          return  "       nvlan: '" + line.split()[4] + "' ,\n"

    elif 'trunk allowed vlan' in line :
          return  "       trunk: true ,\n" + "       vlan: '" + line.split()[4] + "' ,\n"

    else:
         return " "

def load_Mgtlines(line):

    if 'description' in line :
        tline = ""
        for i in xrange(1,len(line.split())):
            tline = tline + " " + line.split()[i]
        return "       description: '" + tline + "' ,\n"

    elif 'vrf' in line :
          return  "       vrf: '" + line.split()[2] + "' ,\n"

    elif 'ip address' in line :
          return  "       ip: '" + line.split()[2] + "' ,\n"

    else:
          return " "

def load_Vlanlines(line):

    if 'description' in line :
        tline = ""
        for i in xrange(1,len(line.split())):
            tline = tline + " " + line.split()[i]
        return "       description: '" + tline + "' ,\n"

    elif 'ip address' in line :
          return  "       ip: '" + line.split()[2] + "' ,\n"

    else:
          return " "


if __name__=='__main__':

    base_dir = "/home/ADSERV/ansible/ansible/"
    hostname = sys.argv[1]

    inFile = base_dir + "CFG/HPN/REPOS/LAB/CURRENT/" + hostname + ".conf"
    outFile = base_dir + "host_vars/" + hostname 


    ifLine = False
    portConf = False
    portEnable = True
    
    ipInt = False
    intEth = False
    intPO = False
    intMgt = False
    intVlan = False
    intDes = False
    vlans = False

    with open(outFile,"w") as ofile:

         with open(inFile,"r") as ifile:

              ofile.write("---\n")
 
              for line in ifile.readlines() :
         	  
                  if 'device: ' in line.strip() :

                     ofile.write("hw_model: " + line.split()[3].replace("("," ").replace(","," ") +" \n")
                     ofile.write("\n")
         	     ofile.write("eos: " + line.split()[4].strip().replace(")"," ") + " \n")
                     ofile.write("\n")

                  elif 'snmp-server location' in line.strip():
         	     ofile.write("snmp_location: " + line.split()[2] + " \n")
         	     ofile.write("\n")
 
                  if 'interface' in line.strip() :
 
                      portConf = True
 
                      if 'Port-Channel' in line.strip() :
                          if not intPO :
                             ofile.write("\n")
                             ofile.write("Port_Channels:\n")
                             intPO = True
			  ofile.write( "   - { int: " + line.split()[1] + " ,\n")
                          
                          if line.split()[1] == 'Port-Channel1' :
                             ofile.write( "       trunk: true ,\n")
 
                      elif 'Ethernet' in line.strip() :
                           if not intEth :
                              ofile.write("\n")
                              ofile.write("Ethernets:\n")
                           intPO = False
 
                           ofile.write("\n")
                           ofile.write( "   - { int: " + line.split()[1] + " ,\n")
                           intEth = True

                      elif 'Management' in line.strip() :
                           if not intMgt :
                              ofile.write("\n")
                              ofile.write("Management:\n")

                           ofile.write("\n")
                           ofile.write( "   - { int: " + line.split()[1] + " ,\n")

                           intPO = False
                           intEth = False
                           intMgt = True

                      elif 'Vlan' in line.strip() :
                           if not intVlan :
                              ofile.write("\n")
                              ofile.write("VlanInts:\n")

                           ofile.write("\n")
                           ofile.write( "   - { int: " + line.split()[1] + " ,\n")

                           intPO = False
                           intEth = False
                           intMgt = False
                           intVlan = True

                  elif 'vlan' in line.split()[0] :

                        if not vlans :
                           ofile.write("\n")
                           ofile.write("Vlans:\n")

                        ofile.write("\n")
                        ofile.write( "   - { vlan_id: " + line.split()[1] + " ,\n")
                        vlans = True

                  elif intPO  :
                       if '!' in line :
                           if not '!!' in line :
                               portConf = False
                               if not portEnable : 
                                  ofile.write( "   enabled: false,\n")
                                  portEnable = True
                               else : 
                                  ofile.write( "   enabled: true,\n")
                               ofile.write( "       change: false }\n")

                       elif 'shutdown' in line :
                             portEnable = False

                       else :
                           ofile.write(load_POlines(line))
                       
                  elif intEth :

                       if '!' in line :
                           if not '!!' in line :
                               portConf = False
                               if not portEnable :
                                  #ofile.write("       channel-group: none ,\n")
                                  ofile.write("       enabled: false,\n")
                                  portEnable = True
                               else :
                                  ofile.write("      enabled: true,\n")
                               ofile.write( "       change: false }\n")

                       elif 'shutdown' in line :
                             portEnable = False

                       else :
                            ofile.write(load_Ethlines(line))

                  elif intMgt :

                       if '!' in line :
                           if not '!!' in line :
                              portConf = False
                              if not portEnable :
                                 ofile.write("       enabled: false,\n")
                                 portEnable = True
                              else :
                                 ofile.write("       enabled: true,\n")
                              ofile.write( "       change: false }\n")
                              ofile.write("\n")

                       elif 'shutdown' in line :
                             portEnable = False

                       else :
                            ofile.write(load_Mgtlines(line))

                  elif intVlan :

                       if '!' in line :
                           if not '!!' in line :
                              portConf = False
                              if not portEnable :
                                 ofile.write("       enabled: false,\n")
                                 portEnable = True
                              else :
                                 ofile.write("       enabled: true,\n")
                              ofile.write( "       change: false }\n")
                              ofile.write("\n")

                       elif 'shutdown' in line :
                             portEnable = False

                       elif 'mac address-table aging-time 30' in line :
                            break
                            
                       else :
                            ofile.write(load_Vlanlines(line))

                  elif vlans :

                       if 'name' in line :
                           ofile.write("       vlan_name: " + line.split()[1] + ",\n")
                           ofile.write( "       change: false }\n")

                       elif 'vrf definition mgmt' in line :
                             vlans = False

         ifile.close()

    ofile.close()
