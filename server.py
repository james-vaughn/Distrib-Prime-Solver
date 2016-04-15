import socket

def possiblePrimeList():
	n = 1
	while True:
		yield n
		n += 2
		if n % 5 == 0:
			n += 2


def makeSocket():
	addr_info = open(connection_info)


if __name__ == "__main__":
	list = possiblePrimeList()
	for i in range(10):
		print(next(list))	
