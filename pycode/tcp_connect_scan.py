import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "196.168.56.102"
src_port = RandShort()
dst_port=80

tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10) #发送SYN包
if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):  # 无回复 表示端口关闭
    print "Closed"
elif(tcp_connect_scan_resp.haslayer(TCP)):  # 回复了
    if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):  # 回复SYN-ACK
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)  # 发送ACK
        print "Open"
    elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):  #
        print "Closed"