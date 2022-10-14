#
# It is also known by using ‘ping command’. An ICMP packet is sent to a host using the IP address and
# if the ICMP echo is received, that means that the host is online and is receiving the signals. For this, 
# it necessary to get all the IP addresses for which you wish to test that the host is connected or not. 
# This method works on the assumption that network devices have ICMP enabled.
#

import subprocess

for ping in range(1,10):
	address = "127.0.0." + str(ping)
	res = subprocess.call(['ping', '-c', '3', address])
	if res == 0:
		print("ping to", address, "OK")
	elif  res == 2: 
		print("No response from", address)
	else:
		print("Ping to", address, "failed!")