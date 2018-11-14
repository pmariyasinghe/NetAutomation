import json
import jsonrpclib
from jsonrpclib import Server
import time
from pprint import pprint

switches = "veos3.lab.ecmwf.int"
username = "admin"
password = "admin"
#lab_switches = ["veos1.lab.ecmwf.int","veos2.lab.ecmwf.int","veos3.lab.ecmwf.int","veos4.lab.ecmwf.int"]

def main():

#    for switches in lab_switches:
#        switch = Server( 'https://%s:%s@%s/command-api' ( username, password, switches ) )
   	switch = Server( 'https://%s:%s@%s/command-api' %
        	            ( username, password, switches ) )

        time.sleep(10)
        print "Executing Show LLDP command on: %s " % switches
        response = switch.runCmds( 1, [ 'show lldp neighbors'] )
	lldpneighbors = response[ 0 ][ 'lldpNeighbors' ]
        ifile =  open('/home/ADSERV/ansible/ansible/CFG/HPN/REPOS/LAB/topology/veos3.lab.ecmwf.int_topology', 'r')
#        topology = [line.split(',') for line in ifile.readlines()]
#        topology = ifile.read().decode("UTF-8")
        
#        jsonResponse=json.loads(ifile.read().decode("UTF-8").replace("u'","'").replace("'","\"").replace(" ",""))
#        jsonData = jsonResponse["Neighbors"]
#        for jitem in jsonData:
        for jitem in (json.loads(ifile.read().decode("UTF-8").replace("u'","'").replace("'","\"").replace(" ",""))["Neighbors"]):

            #print item.get("port")
            #print item.get("neighborDevice")

        #print lldpneighbors
#        for k in topology:
#            print k[1][1]
            for litem in lldpneighbors:
                if [litem][0]['port'] == jitem.get("port"): 
                   #print [litem][0]['neighborDevice']
                   print "Neighbor %s is connected to %s " % ( [litem][0]['neighborDevice'], [litem][0]['port'] )
                   #if j[1][0] == [i][0]['port'] :
                   #   print j[1][0]
                   ##print "Neighbor %s is connected to %s " % ( neighDev, port )

if __name__ == '__main__':
   main()
