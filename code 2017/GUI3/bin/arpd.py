# Refrence
# https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

import os
import socket
from struct import unpack
import binascii
import sys
from share import add_ip_port_to_block,change_flag,add_logdata,add_ip_mac
from notification import notification
class Sniffer():
	def __init__(self):
		"""
			0x0003 for all packets sniffing
		"""
		try:
			open('sfile.db')
		except:
			import initiate
		print '  Use -h option for help(?)'
		try:
			self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
		except socket.error , msg:
			print 'Socket Error Code : ' + str(msg[0]) + ' Message : ' + msg[1]
			sys.exit(0)
		self.iptomacmap=dict()	
		self.verbose_arp=False
		self.verbose_icmp=False
		self.verbose_tcp=False
		self.verbose_udp=False
		self.verbose_imt=False
		self.verbose_notification=False
		self.gui=False
		if '-h' in sys.argv:
			print """
	Welcome(Tool)
	This Tool is designed to secure Network from sniffing etc...
	Edited in python 2.7
	
	Usage: python tool.py [options]
	-h : help (default False)
	-v : Verbose mode (default False)[ show all stdout options ]
	-i [xxx.xxx.xxx.xxx]: block specific ip
	-p [n]: block specific port Range [0-65535]
	-i [xxx.xxx.xxx.xxx] -p [n] : block specific (ip:port)
	-tcp : show only tcp packets
	-udp : show only udp packets
	-icmp : show only icmp packets
	-arp : show only arp pakcets
	-n : show notifications
	-t : show ip-mac map table

			""" 
			sys.exit(0)
		else:
			print 'Sniffing detection started ...'
		if '-arp' in sys.argv:
			self.verbose_arp(True)
		if '-icmp' in sys.argv:
			self.verbose_icmp=True
		if '-tcp' in sys.argv:
			self.verbose_tcp=True
		if '-udp' in sys.argv:
			self.verbose_udp=True
		if '-t' in sys.argv:
			self.verbose_imt=True
		if '-n'	in sys.argv:
			self.verbose_notification=True
		if '-i' in sys.argv or '-p' in sys.argv:
			ip=''
			port=''
			if '-i' in sys.argv:
				try:
					ip=sys.argv[sys.argv.index('-i')+1]
				except:
					print 'Try correct ip address Ex. 192.168.147.27'
					sys.exit(0)
			if '-p' in sys.argv:
				try:
					port=sys.argv[sys.argv.index('-p')+1]
				except:
					print 'Try correct port range 0-65535 Ex. 8080'
					sys.exit(0)
			self.block_ip(ip=ip,port=port)
			sys.exit(0)
		if '-v' in sys.argv:
			self.verbose_udp=True
			self.verbose_tcp=True
			self.verbose_icmp=True
			self.verbose_arp=True
			self.verbose_imt=True
	def eth_addr(self,addr):
		return "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(addr[0]) , ord(addr[1]) , ord(addr[2]), ord(addr[3]), ord(addr[4]) , ord(addr[5]))
	def getProtocol(self,number):
		"""
			Return string of Protocol Number respectively
		"""
		if number==1:
			return 'ICMP PROTOCOL'
		elif number==8:
			return 'EGP PROTOCOL'
		return str(number)
	def push_notification(self,notification):
		if self.verbose_notification:
			notification(notification)
	def block_ip(self,ip='',port=''):
		if(ip and port):
			os.system('iptables -A INPUT -s '+ip+' -p '+port+' -j DROP')
			os.system('iptables -A OUTPUT -s '+ip+' -p '+port+' -j DROP')
			text='IP : '+str(ip)+' Port : '+str(port)+' is blocked.'
		elif(ip):
			os.system('iptables -A INPUT -s '+ip+' -j DROP')
			os.system('iptables -A OUTPUT -d '+ip+' -j DROP')
			text='IP : '+str(ip)+' is blocked.'
		else:
			os.system('iptables -A INPUT -p '+port+' -j DROP')
			text=' Port : '+str(port)+' is blocked.'
		add_ip_port_to_block(ip,port)
		self.push_notification(text)
	def print_mapiptomac(self):
		for i in self.iptomacmap.keys():
			print "{:16} : {}".format(i,self.iptomacmap[i])
	def map_ip_to_mac(self,ip,mac):
		try:
			if mac not in self.iptomacmap[ip] and mac!='00:00:00:00:00:00' and ip!='0.0.0.0':
				self.iptomacmap[ip].append(mac)
		except:
			if mac!='00:00:00:00:00:00' and ip!='0.0.0.0':
				self.iptomacmap[ip]=[mac]
		if ip!='0.0.0.0' and mac!='00:00:00:00:00:00':
			add_ip_mac(ip,mac)
		if self.verbose_imt:
			print "{:16} : {}".format(ip,mac)
	def tcp_protocol(self,packet,tcp_length):
		# TCP
		# TRANSMISSION CONTROL PROTOCOL
		#
		tcp_header = unpack('!HHLLBBHHH' , packet[tcp_length:tcp_length+20])
		source_port = tcp_header[0]
		dest_port = tcp_header[1]
		sequence_number = tcp_header[2]
		ack_number = tcp_header[3]
		data_offset = tcp_header[4]
		tcp_header_length = data_offset >> 4
		data_start = tcp_length + tcp_header_length*4
		data_size = len(packet)-data_start
		tcp_string='TCP Protocol\nSource Port            : '+str(source_port)+'\nDestination Port       : '+str(dest_port)+'\nSequence Number        : '+str(sequence_number)+'\nAcknowledgement Number : '+str(ack_number)+'\nData Offset            : '+str(data_offset)+'\nTCP Header Length      : '+str(tcp_header_length)
		if packet[data_start:]:
			tcp_string+='\nData                   : '+str(packet[data_start:])+'\n'
		add_logdata(text)
		if self.gui:
			tcp_string=''
		return tcp_string
	def icmp_protocol(self,packet,icmp_length):
		# ICMP
		# INTERNET CONTROL MESSAGE PROTOCOL
		#
		icmp_header = unpack('!BBH' , packet[icmp_length:icmp_length+4])
		icmp_type = icmp_header[0]
		icmp_code = icmp_header[1]
		icmp_checksum = icmp_header[2]
		data_start = icmp_length + 4
		data_size = len(packet) - data_start
		icmp_string='ICMP Protocol'+'\nType     : '+str(icmp_type)+'\nCode     : '+str(icmp_code)+'\nChecksum : '+str(icmp_checksum)
		if packet[data_start:]:
			icmp_string+='\nData     : '+str(packet[data_start:])+'\n'
		add_logdata(icmp_string)
		if self.gui:
			icmp_string=''
		return icmp_string
	def udp_protocol(self,packet,udp_length):
		# UDP
		#
		#
		udp_header = unpack('!HHHH',packet[udp_length:udp_length+8])
		source_port = udp_header[0]
		dest_port = udp_header[1]
		udp_length = udp_header[2]
		udp_checksum = udp_header[3]
		data_start = udp_length + 8
		data_size = len(packet) -data_start
		udp_string='UDP Protocol'+'\nSource Port      : '+str(source_port)+'\nDestination Port : '+str(dest_port)+'\nLength           : '+str(udp_length)+'\nChecksum         : '+str(udp_checksum)
		if packet[data_start:]:
			udp_string+='\nData             : '+str(packet[data_start:])+'\n'
		add_logdata(udp_string)
		if self.gui:
			udp_string=''
		return udp_string
	def arp_protocol(self,packet):
		# ARP
		#
		#
		arp_header=unpack("2s2s1s1s2s6s4s6s4s",packet[14:42])
		sip = socket.inet_ntoa(arp_header[6])
		smac= self.eth_addr(arp_header[5])
		dip = socket.inet_ntoa(arp_header[8])
		dmac= self.eth_addr(arp_header[7])
		self.map_ip_to_mac(sip,smac)
		self.map_ip_to_mac(dip,dmac)
		arp_string=''
		if self.verbose_arp:
			arp_string='ARP Protocol'+"\nHardware type : "+str(binascii.hexlify(arp_header[0]))+"\nProtocol type : "+str(binascii.hexlify(arp_header[1]))+"\nHardware size : "+str(binascii.hexlify(arp_header[2]))+"\nProtocol size : "+str(binascii.hexlify(arp_header[3]))+"\nOpcode        : "+str(binascii.hexlify(arp_header[4]))+"\nSource MAC    : "+str(smac)+"\nSource IP     : "+str(sip)+"\nDest MAC      : "+str(dmac)+"\nDest IP       : "+str(dip)+'\n'
			add_logdata(arp_string)
		if self.gui:
			arp_string=''
		return arp_string
	def sniff_packet(self):
		packet_raw=self.sock.recvfrom(65565)
		packet=packet_raw[0]
		header_length=14
		header=unpack('!6s6sH' , packet[0:header_length])
		protocol=socket.ntohs(header[2])
		if self.verbose_arp or self.verbose_udp or self.verbose_tcp or self.verbose_icmp:
			print '\n------------------------------------------------' + '\nDestination MAC : ' + self.eth_addr(packet[0:6]) + '\nSource MAC      : ' + self.eth_addr(packet[6:12]) + '\nProtocol        : ' + self.getProtocol(protocol)+'\n'
		if protocol==8 and (self.verbose_udp or self.verbose_tcp or self.verbose_icmp):
			# EGP
			# Exterior Gateway Protocol
			#
			eth_header=unpack('!BBHHHBBH4s4s',packet[header_length:header_length+20])
			version = eth_header[0] >> 4
			eth_header_length = eth_header[0] & 0xF
			protocol2 = eth_header[6]
			string='EGP Version : '+str(version)+'\nIP Header Length : '+str(eth_header_length)+'\nProtocol : '+str(self.getProtocol(protocol2))+'\n'
			if self.gui:
				add_logdata(string)
			else:	
				print string
			if protocol2 == 1 and self.verbose_icmp:
				print self.icmp_protocol(packet,header_length+eth_header_length*4)
			elif protocol2 == 6 and self.verbose_tcp:
				print self.tcp_protocol(packet,header_length+eth_header_length*4)
			elif protocol2 == 17 and self.verbose_udp:
				print self.udp_protocol(packet,header_length+eth_header_length*4)
			else:
				pass
				#print 'not implement this protocol No.',protocol2
		elif protocol==1544:
			print self.arp_protocol(packet)
		return packet