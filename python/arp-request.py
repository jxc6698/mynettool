import sys
import struct
import os
import socket
import string


#ETH_TARGET = '\x00\xe0\x4c\x53\x44\x58'
#another_IP = "114.212.87.245"

#ETH_TARGET = '\x00\x23\x9c\xde\xd5\x28'
#another_IP = "114.212.86.125"

ETH_BROADCAST = '\xff\xff\xff\xff\xff\xff'
another_IP = "114.212.86.120"


net_CARD = 'eth0'

ETH_ZERO = '\x00\x00\x00\x00\x00\x00'
ETH_TYPE_ARP= 0x0806
ARP_REQUEST = 1
ARP_REPLY = 2


# act as the other one
false_IP = "114.212.80.1"

sender_IP = '114.212.86.126'


def send_arp( ifname , address ):
	""" send out a arp """
	try:
		eth_socket =  socket.socket( socket.AF_PACKET , socket.SOCK_RAW) ;
		eth_socket.bind( (ifname , ETH_TYPE_ARP) ) ;
		print eth_socket.getsockname() ;
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

		struct.pack("!h" , ARP_REQUEST ) ,# request

		eth_addr ,   #  sender

		socket.inet_aton( sender_IP ) ,  # sender

		ETH_ZERO,

		socket.inet_aton( another_IP )
	]

	eth_frame = [
		ETH_BROADCAST,

		eth_addr ,
		struct.pack("!h" , ETH_TYPE_ARP ),
		''.join( arp_frame )

	]

	eth_socket.send(''.join(eth_frame) );
	eth_socket.close();



if __name__ == '__main__':
	send_arp( net_CARD , false_IP );
	print "lllll"

