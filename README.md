Network Automation lab

For this lab, I created a self-contained virtual environment with CentOS Linux/KVM, vagrant and Arista virtual EOS (vEOS). 
Here I’m trying to address all of the technically challenges when a network needs to be built programmatically. I think building 
a network from the ground up level programmatically is important as much as maintaining it programmatically. Python is the 
programming language which I used for as my base scripting and although I didn’t have much experience with Python and managed to 
suss out most of concepts including object oriented programming. This will allow us to build the network based on the backup 
configuration in case of disaster.  

virtual hosts used in my lab:
- Ansible host: vagrant-ubuntu-trusty-64
- Management host: CentOS Linux release 7.3.1611 (Core). 
  Services running on this host are DHCP and TFTP.
- L3 and L2 switches: Arista veos 4.17.8M   

This Network automation lab contains a number of playbooks which represent the following action
• Zero touch provisioning 
  o Generate config templates for SPINE and LEAF switches based on initial attributes define in host file.
  o Push the configuration templates to the TFTP server
  o Update DHCP config entries for each network host using its Management interface’s MAC address with and restart DHCP server
  o The network host in its initial boot downloads a python script from the TFTP server to and execute the given instructions in the script. 
    This script checks it’s system MAC address and download the relevant configuration template to the host including the correct firmware. 
	
• Validate LLDP neighbours
• Build topology


- 
