import socket
import sys
try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as msg:
	print('Failed to create socket. Error Code:'+str(msg[0]+' Error Message:'+str(msg[0])))
	sys.exit()
host=str(input('Enter Host Name : '))
try:
	ip=socket.gethostbyname(host)
except:
	print("Hostname could't resolve!")
	sys.exit()
print('\nHost : '+str(host))
print('IP   : '+str(ip))