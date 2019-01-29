#!/usr/bin/env python

from paramiko import SSHClient
from scp import SCPClient
 
def progress(filename, size, sent):
    print filename + " " + str(size) + " " + str(sent)
 
if __name__ == "__main__":
 
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('monitora', port=22, username="", password="")
 
    # SCPCLient takes a paramiko transport as its only argument
    # Just a no-op. Required sanitize function to allow wildcards.
    scp = SCPClient(ssh.get_transport(), sanitize=lambda x: x, progress=progress)
 
    # scp.listdir("/var/tmp")
    scp.get("/home/ADSERV/glibc-2.11.1-0.18.2.x86_64.rpm")
