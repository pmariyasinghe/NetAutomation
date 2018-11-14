import json
import jsonrpclib
from jsonrpclib import Server

switches = "veos2.lab.ecmwf.int"
username = "admin"
password = "admin"

def main():
   switch = Server( 'https://%s:%s@%s/command-api' %
                    ( username, password, switches ) )
   response = switch.runCmds( 1, [ 'show interfaces' ] )
   print response
   interfaces = response[ 0 ][ 'interfaces' ]
   for intf, value in interfaces.iteritems():
      mtu = [value][0]['mtu']
      print "Interface %s has its MTU set to %i" % ( intf, mtu )

if __name__ == '__main__':
   main()
