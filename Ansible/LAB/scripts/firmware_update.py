import json
import jsonrpclib
from jsonrpclib import Server
import time
from pprint import pprint
import sys

switches = sys.argv[1]
username = sys.argv[3]
password = sys.argv[4]
#lab_switches = ["veos1.lab.ecmwf.int","veos2.lab.ecmwf.int","veos3.lab.ecmwf.int","veos4.lab.ecmwf.int"]

def main():

#    for switches in lab_switches:
   	switch = Server( 'https://%s:%s@%s/command-api' %
        	            ( username, password, switches ) )

        time.sleep(10)

        sys.stdout = open("/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/LAB/LOG/" + switches + "_firmware-update.log",'a')

	print "############################ Firmware Update #############################"
	print "Date and Time : " + time.strftime("%x") + " " + time.strftime("%X")
	print "Checked by : " +  username
	print "\n"

        print "Executing Show LLDP command on: %s " % switches
        response = switch.runCmds( 1, [ 'show lldp neighbors'] )
	lldpneighbors = response[ 0 ][ 'lldpNeighbors' ]
#        ifile =  open('/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/LAB/topology/veos2.lab.ecmwf.int_topology', 'r')
        ifile = open(sys.argv[2],'r')
#        ifile = sys.argv[2].strip()
        for jitem in (json.loads(ifile.read().decode("UTF-8").replace("u'","'").replace("'","\"").replace(" ",""))["Neighbors"]):
#        for jitem in (json.loads(ifile.decode("UTF-8").replace("u'","'").replace("'","\"").replace(" ",""))["Neighbors"]):

            for litem in lldpneighbors:
                if ([litem][0]['port'] == jitem.get("port")):
                   if ([litem][0]['neighborDevice'] == jitem.get("neighborDevice")):
                      print "Neighbor %s is connected to %s ---> Topology Validation %s" % ( [litem][0]['neighborDevice'], [litem][0]['port'], '= PASS' )
                      if ([litem][0]['neighborPort'] == jitem.get("neighborPort")):
                         print "I'm connected to Neighbor %s port %s ---> Topology Validation %s\n" % ( [litem][0]['neighborDevice'], [litem][0]['neighborPort'], '= PASS' )
                      else:
                         print "I'm connected to Neighbor %s port %s ---> Topology Validation %s\n" % ( [litem][0]['neighborDevice'], [litem][0]['neighborPort'], '= FAIL' )
                   else:
                      print "Neighbor %s is connected to %s ---> Topology Validation %s" % ( [litem][0]['neighborDevice'], [litem][0]['port'], '= FAIL' )
        ifile.close()
        print "\n"
        print "\n"

if __name__ == '__main__':
   main()
