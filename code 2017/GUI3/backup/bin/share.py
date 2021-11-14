# 	BLOCKED TABLE
#  _______________
# |ID | IP | PORT |
# -----------------
# 	FLAG TABLE
#  ___________________________________________________________________
# | ICMP | TCP | ARP | UDP | BACKGROUND | AUTOBLOCKING | NOTIFICATION |
# ---------------------------------------------------------------------

import sqlite3
def add_ip_port_to_block(ip,port):
	file=sqlite3.connect('sfile.db')
	file.execute("INSERT INTO BLOCKED (IP,PORT) VALUES ('"+ip+"',"+str(port)+");")
	file.commit()
	file.close()	
def change_flag(icmp=False,tcp=False,arp=False,udp=False,background=False,autoblocking=False,notification=False):
	file=sqlite3.connect('sfile.db')
	file.execute("UPDATE FLAG SET ICMP="+icmp+",TCP="+tcp+",ARP="+arp+",UDP="+udp+",BACKGROUND="+background+",AUTOBLOCKING="+autoblocking+",NOTIFICATION="+notification+");")
	file.commit()
	file.close()
def add_ip_mac(ip,mac):
	file=sqlite3.connect('sfile.db')
	file.execute("INSERT INTO MACIP (IP,MAC) VALUES ('"+ip+"',"+str(mac)+");")
	file.commit()
	file.close()
def add_logdata(text):
	file=open('logfile','aw')
	file.write(text)
	file.close()
