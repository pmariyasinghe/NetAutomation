import paramiko
from paramiko import SSHClient
from scp import SCPClient
 
########################################################################
class SCPConnection(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, hostname, username, password, port=22):
        """Initialize and setup connection"""
 
        self.scp = None
        self.scp_open = False
 
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=hostname, port=port, username=username , password=password)


    #----------------------------------------------------------------------
    def _openSCPConnection(self):
        """
        Opens an SCP connection if not already open
        """
        if not self.scp_open:
            self.scp = SCPClient(self.ssh.get_transport())
            self.scp_open = True
 
    #----------------------------------------------------------------------
    def get(self, remote_path, local_path=None):
        """
        Copies a file from the remote host to the local host.
        """
        self._openSCPConnection()        
        self.scp.get(remote_path, local_path)        
 
    #----------------------------------------------------------------------
    def put(self, local_path, remote_path=None):
        """
        Copies a file from the local host to the remote host
        """
        self._openSCPConnection()
        self.scp.put(local_path, remote_path)
 
    #----------------------------------------------------------------------
    def close(self):
        """
        Close SCP connection and ssh connection
        """
        if self.scp_open:
            self.scp.close()
            self.scp_open = False
        self.ssh.close()
