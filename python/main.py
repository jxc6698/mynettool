#Packet sniffer in python for Linux
#Sniffs only incoming TCP packet


# tcpdump can be used like this
# sudo tcpdump -i eth2 host 219.219.114.15 and port 80

import socket, sys
from struct import *
#from scapy.all import ETH_P_ALL

#create an INET, STREAMing socket
try:
#	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_IP)
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons( 0x0003 ) ) ;
except socket.error as msg:
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()


eth_head = 14 ;
BRAS_IP= '219.219.114.15' ;

# receive a packet
while True:
	packet = s.recvfrom(65565)   # recvfrom return data , address
	
	#packet string from tuple
	packet = packet[0]
	
	#take first 20 characters for the ip header
	ip_header = packet[0+eth_head:20+eth_head]
	
	#now unpack them :)
	iph = unpack('!BBHHHBBH4s4s' , ip_header)
	
	version_ihl = iph[0]
	version = version_ihl >> 4
	ihl = version_ihl & 0xF
	
	iph_length = ihl * 4
	
	ttl = iph[5]
	protocol = iph[6]
	s_addr = socket.inet_ntoa(iph[8]);
	d_addr = socket.inet_ntoa(iph[9]);
	
#	print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
	
	if( d_addr == BRAS_IP  ) :

		tcp_header = packet[iph_length+eth_head:iph_length+20+eth_head] #now unpack them :)
		tcph = unpack('!HHLLBBHHH' , tcp_header)
	
		source_port = tcph[0]
		dest_port = tcph[1]
		sequence = tcph[2]
		acknowledgement = tcph[3]
		doff_reserved = tcph[4]
		tcph_length = doff_reserved >> 4
		
#		print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
		
		h_size = iph_length + tcph_length * 4
		data_size = len(packet) - h_size
		
		#get data from the packet
		data = packet[h_size:]
		
#  not print data
#	print 'Data : ' + data
		
		if( str(dest_port) == '80' ):
			index =  data.find( 'action=login') ;
			print "index %d " %  index
			if( index >= 0 ) :
				print data[ index: ] ;

