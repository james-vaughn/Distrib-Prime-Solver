import socket


NUM_CONNECTIONS = 5

def possiblePrimeList():
	n = 1
	while True:
		yield n
		n += 2
		if n % 5 == 0:
			n += 2


def makeSocket():
	host_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	host_info = []
	with open(connection_info) as addr_info:
		host_info = addr_info.readlines()

	port = host_info[1]
	try:
		host_sock.bind( ('',port) )
		return host_sock
	except socket.error as msg:
		print("FUCK: "+msg)
			


if __name__ == "__main__":
	host_sock = makeSocket()
	host_sock.listen(NUM_CONNECTIONS)
	
	while True:
		conn, addr = host_sock.accept()
		host_sock.sendall("Hello to "+conn+":"+addr)
	#l = possiblePrimeList()

	#for i in range(10):
	#	host_sock.send(next(list))	
