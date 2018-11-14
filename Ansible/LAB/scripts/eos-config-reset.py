import jsonrpclib
from jsonrpclib import Server
import time

username = sys.argv[1]
switches = sys.argv[2]
password = sys.argv[3]

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

