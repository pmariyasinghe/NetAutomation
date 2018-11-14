import json
import jsonrpclib
from jsonrpclib import Server
import time

switches = "veos1.lab.ecmwf.int"
username = "admin"
password = "admin"
#lab_switches = ["veos1.lab.ecmwf.int","veos2.lab.ecmwf.int","veos3.lab.ecmwf.int","veos4.lab.ecmwf.int"]

def main():

#    for switches in lab_switches:
        switch = Server( 'https://%s:%s@%s/command-api' %
                            ( username, password, switches ) )

        time.sleep(10)
        print "Erasing configuration on : %s " % switches
        response = switch.runCmds( 1, [ 'erase startup-config'] )
        time.sleep(10)
        print "Reloading : %s " % switches + "....."
        response = switch.runCmds( 1, [ 'reload now' ] )

if __name__ == '__main__':
   main()
