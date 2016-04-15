import socket

def connectToHost(sock):
	host_info = []

	with open("connection_info") as addr_info:
		host_info = addr_info.readlines()

	host_ip = host_info[0]
	host_socket = int(host_info[1])

	sock.connect( (host_ip,host_socket) )

if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connectToHost(sock)

	print(sock.recv(4096))
