import socket
from concurrent.futures import ThreadPoolExecutor

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
	with open("connection_info") as addr_info:
		host_info = addr_info.readlines()

	port = int(host_info[1])
	try:
		host_sock.bind( ('',port) )
		return host_sock
	except socket.error as msg:
		print("FUCK: "+msg)
			

def echo(connSock):
	connSock.send("Begin echoing".encode('utf-8'))

	while True:
		msg = connSock.recv(4096)
		connSock.send(msg)
	


if __name__ == "__main__":
	pool = ThreadPoolExecutor(max_workers=NUM_CONNECTIONS)
	
	host_sock = makeSocket()
	host_sock.listen(NUM_CONNECTIONS)
	
	while True:	
		conn, addr = host_sock.accept()
		print("Connection from "+addr[0]+":"+str(addr[1]))
	
		pool.submit(echo,conn)


	#l = possiblePrimeList()

	#for i in range(10):
	#	host_sock.send(next(list))	
