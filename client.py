import socket

def connectToHost(sock):
	host_info = []

	with open("connection_info") as addr_info:
		host_info = addr_info.readlines()

	host_ip = host_info[0]
	host_socket = int(host_info[1])

	sock.connect( (host_ip,host_socket) )


def isPrime(num):
	
	r = int(num**0.5)
	f = 3
	while f <= r:
		if num%f == 0: 
			return "False"
		f +=2
	return "True"  


if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connectToHost(sock)

	print( sock.recv(4096).decode('utf-8') )
	sock.send( "Ready".encode('utf-8') )
	
	#begin actual work
	while True:
		print("waiting...")
		num = int( sock.recv(4096).decode('utf-8') )
		print("Working on {}".format(num))
		result = isPrime(num)
		sock.send( result.encode('utf-8'))

