
#!/user/bin/env python3
#Cisco Config pulling using telnet

import getpass
import telnetlib

user = input("Enter your Telnet Username: ")
password = getpass.getpass()

#Opening a file where we saved devives IP information
f = open("Mydevices")

#Looping to get access to all the devicess and pull informations
for IP in f:
	IP = IP.strip()
    print ("Pulling Running Config" + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")

	if password:
		tn.read_until(b"Password: ")
    	tn.write(password.encode('ascii') + b"\n")
#Cisco Commands
    tn.write(b"terminal length 0\n")
    tn.write(b"show envirnment\n")
    tn.write(b"show inventory\n")
    tn.write(b"show dir\n")
    tn.write(b"show run\n")
    tn.write(b"show ip int bri\n")
    tn.write(b"exit\n")

#Saving output in a new file for each 
    readoutput = tn.read_all()
    saveoutput = open("TEST_Device_" + HOST, "w")
    saveoutput.write(readoutput.decode("ascii"))
    saveoutput.write("\n")
    saveoutput.close
#Print output in cli of Network Automation Container
    print(tn.read_all().decode('ascii'))
