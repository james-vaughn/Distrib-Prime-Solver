import socket
from concurrent.futures import ThreadPoolExecutor

NUM_CONNECTIONS = 50

def possiblePrimeList(start):
	n = start if start%2==1 else start+1
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
			

numList = possiblePrimeList(2000000000000000)

#function for dispatching potential primes to clients
def distribNums(connSock):
	connSock.send("Beginning transmission of potential primes".encode('utf-8'))
	connSock.recv(4096) #wait for the ready signal
	while True:
		num = next(numList)	
		connSock.send( str(num).encode('utf-8') )
		result = connSock.recv(4096).decode('utf-8')
		if result=='True':
			print("{} identified as a prime".format(num))


#echo server for testing
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
	
		pool.submit(distribNums,conn)

