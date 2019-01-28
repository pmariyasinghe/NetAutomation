import json
import jsonrpclib
from jsonrpclib import Server
import time
from pprint import pprint
import sys
import yaml

switches = sys.argv[1]
#username = sys.argv[3]
password = sys.argv[3]
username = "admin"
#password = "admin"

#lab_switches = ["LEAF01","LEAF02","LEAF03","SPINE01","SPINE02"]

def main():

#    for switches in lab_switches:
   	switch = Server( 'https://%s:%s@%s/command-api' %
        	            ( username, password, switches ) )
        
        time.sleep(10)

        sys.stdout = open("/vagrant/NetAutomation/Ansible/LAB/ConfigRepos/LOGS/" + switches + "_topology.log",'a')

	print "############################ Show LLDP Neighbors #############################"
	print "Date and Time : " + time.strftime("%x") + " " + time.strftime("%X")
	print "Checked by : " +  username
	print "\n"

        print "Executing Show LLDP command on: %s " % switches
        response = switch.runCmds( 1, [ 'show lldp neighbors'] )
	lldpneighbors = response[ 0 ][ 'lldpNeighbors' ]
        ifile = open(sys.argv[2],'r')
#        ifile = open("/vagrant/NetAutomation/Ansible/LAB/ConfigRepos/topology/" + switches + "_topology", 'r')   
        jneighbors = json.loads(ifile.read().decode("UTF-8").replace("u'","'").replace("'","\"").replace(" ",""))["Neighbors"]
#        print jneighbors
        for jitem in jneighbors:
            for litem in lldpneighbors:
                if ([litem][0]['port'] == jitem.get("port")):
                   if ([litem][0]['neighborDevice'] == jitem.get("neighborDevice")):
                      print "Neighbor %s is connected to %s ---> Topology Validation %s" % ( [litem][0]['neighborDevice'], [litem][0]['port'], '= PASS' )
                      jitem["validation"] = "PASS"
                      if ([litem][0]['neighborPort'] == jitem.get("neighborPort")):
                         print "I'm connected to Neighbor %s port %s ---> Topology Validation %s\n" % ( [litem][0]['neighborDevice'], [litem][0]['neighborPort'], '= PASS' )
                      else:
                         print "I'm connected to Neighbor %s port %s ---> Topology Validation %s\n" % ( [litem][0]['neighborDevice'], [litem][0]['neighborPort'], '= FAIL' )
                         jitem["validation"] = "FAIL"
                   else:
                      print "Neighbor %s is connected to %s ---> Topology Validation %s" % ( [litem][0]['neighborDevice'], [litem][0]['port'], '= FAIL' )
                      jitem["validation"] = "FAIL"
        ifile.close()
        ofile = open("/vagrant/NetAutomation/Ansible/LAB/ConfigRepos/topology/" + switches + "_topology", 'w')
        ofile = open(sys.argv[2],'w')
        json.dump(jneighbors,ofile)
        ofile.close()
        print "\n"
        print "\n"

if __name__ == '__main__':
   main()
