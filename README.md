Network Automation lab

Please note my lab is pretty much similar to LAB topolgy used in the following link.

https://the-bitmask.com/2017/07/11/arista-veos-l3slv-part1/

Whole idea behind designing a lab using vEOS, VXLAN and KVM was encouraged by above Pablo Narváez's great article. Therefore Hats off to 
Pablo who did a great job putting this article together making it everyone to create a LAB environment in virtual environments more 
effective manner.

Topoloy diagram:
![alt text](https://github.com/pmariyasinghe/NetAutomation/tree/master/vxlan-fabric-netwokdiagram.png?raw=true)

../blob/master/myimage.png?raw=true

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

This Network automation lab contains a number of playbooks which represent the following action.

- Zero touch provisioning
 
  - Generate config templates for SPINE and LEAF switches based on initial attributes define in host file.
  - Push the configuration templates to the TFTP server.
  - Update DHCP config entries for each network host using its Management interface’s MAC address with and restart DHCP server.
  - The network host in its initial boot downloads a python script from the TFTP server to and execute the given instructions in the script. 
    This script checks it’s system MAC address and download the relevant configuration template to the host including the correct firmware. 
	
- Validate LLDP neighbours

- Build topology

- 
