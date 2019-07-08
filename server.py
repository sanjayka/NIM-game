import socket
import time


def print_game(lis):
	st = "Current game status.\n"
	st = st+("     ")+("| "*lis[0])+(". "*(3-lis[0]))+"\n"
	st = st+("   ")+("| "*lis[1])+(". "*(5-lis[1]))+"\n"
	st = st+(" ")+("| "*lis[2])+(". "*(7-lis[2]))+"\n"
	st = st+"\n"
	print(st)
	c.send((st).encode())
	time.sleep(1)


def play_game(lis):
	if(turn == 0):
		print("Enter your move.")
		a,b=map(int,list(input().split(" ")))

		if(lis[a-1] < b):
			print("Invalid move.")
			return 0

		else:
			print("Move played.")
			lis[a-1] -= b
			return 1
	else:
		st="Enter your move.\n"
		#c.send((st).encode())
		inp = c.recv(100).decode()
		time.sleep(1)
		a,b=map(int,list(inp.split(" ")))

		if(lis[a-1] < b):
			st="Invalid move.\n"
			c.send((st).encode())
			time.sleep(1)
			return 0

		else:
			st="Move played.\n"
			c.send((st).encode())
			time.sleep(1)
			lis[a-1] -= b
			return 1

def game_status(lis):
	for i in lis:
		if(i != 0):
			return 0
	return 1

lis = [3,5,7]
turn = 0
# creating a socket to listen for incoming connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding hostname and port number to socket
serversocket.bind(('',8828))
serversocket.listen(1)
c, addr = serversocket.accept()
#print("Connected to client")
#print(addr[1])

st = "Enter your name:"
print(st)
c.send((st).encode())
time.sleep(1)
server = input()
client = c.recv(100)
time.sleep(1)

st = "The players are : "+server+" , "+client.decode()+"\n"
print(st)
c.send((st).encode())
time.sleep(1)
players = [server,client.decode()]
print_game(lis)

while(game_status(lis) != 1):
	st = "It is "+players[turn]+"'s turn."+"\n"
	print(st)
	c.send((st).encode())
	time.sleep(1)
	x = play_game(lis)
	print_game(lis)
	if(x==1):
		turn = (turn+1)%2

if(turn == 0):
	st = players[1] + " lost the game."+"\n"
	print(st)
	c.send((st).encode())
	time.sleep(1)
else:
	st = players[0] + " lost the game."+"\n"
	print(st)
	c.send((st).encode())
	time.sleep(1)
 # receive only 50 at a time
c.close()
