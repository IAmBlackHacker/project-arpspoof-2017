# 	BLOCKED TABLE
#  _______________
# |ID | IP | PORT |
# -----------------
# 	FLAG TABLE
#  ___________________________________________________________________
# | ICMP | TCP | ARP | UDP | BACKGROUND | AUTOBLOCKING | NOTIFICATION |
# ---------------------------------------------------------------------

import sqlite3


def add_ip_port_to_block(ip, port):
    file = sqlite3.connect('sfile.db')
    try:
        query="INSERT INTO BLOCKED (IP,PORT) VALUES ('" + str(ip) + "'," + str(port) + ");"
        file.execute(query)
        file.commit()
    except:
        print 'invalid ip,port'
        return False
    file.close()
    return True


def change_flag(icmp=False, tcp=False, arp=False, udp=False, background=False, autoblocking=False, notification=False):
    file = sqlite3.connect('sfile.db')
    query = "UPDATE FLAG SET ICMP='" + str(icmp) + "',TCP='" + str(tcp) + "',ARP='" + str(arp) + "',UDP='" + str(
        udp) + "',BACKGROUND='" + str(background) + "',AUTOBLOCKING='" + str(autoblocking) + "',NOTIFICAIION='" + str(
        notification) + "'"
    file.execute(query)
    file.commit()
    file.close()


def add_ip_mac(ip, mac):
    file = sqlite3.connect('sfile.db')
    file.execute("INSERT INTO MACIP (IP,MAC) VALUES ('" + ip + "','" + str(mac) + "');")
    file.commit()
    file.close()


def add_logdata(text):
    file = open('logfile', 'a')
    file.write(text)
    file.close()


def flush_tables():
    open('logfile','w').write('')
    file = sqlite3.connect('sfile.db')
    file.execute("delete from macip;")
    file.execute("delete from blacklist;")
    file.commit()
    file.close()

def get_flags():
    file = sqlite3.connect('sfile.db')
    data=file.execute("SELECT * FROM FLAG").fetchall()[0]
    file.commit()
    file.close()
    n=['icmp','tcp','arp','udp','imt','background','autoblocking','notification']
    fdata=dict()
    for i in range(len(n)):
        if data[i]==u'True':
            fdata[n[i]]=True
        else:
            fdata[n[i]]=False
    return fdata