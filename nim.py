def print_game(lis):
	st = "Current game status.\n"
	st = st+("     ")+("| "*lis[0])+(". "*(3-lis[0]))+"\n"
	st = st+("   ")+("| "*lis[1])+(". "*(5-lis[1]))+"\n"
	st = st+(" ")+("| "*lis[2])+(". "*(7-lis[2]))+"\n"
	st = st+"\n"
	print(st)

def play_game(lis):
	print("Enter your move.")
	a,b=map(int,list(input().split(" ")))

	if(lis[a-1] < b):
		print("Invalid move.")
		return 0

	else:
		lis[a-1] -= b
		return 1

def game_status(lis):
	for i in lis:
		if(i != 0):
			return 0
	return 1

lis = [3,5,7]
print_game(lis)
print("Enter Player1's name:")
players[0] = input()
print("Enter Player2's name:")
players[1] = input()
turn = 0

while(game_status(lis) != 1):
	print("It is "+players[turn]+"\'s turn.")
	x = play_game(lis)
	print_game(lis)
	if(x==1):
		turn = (turn+1)%2

if(turn == 0):
	print(players[1] + " lost the game.")
else:
	print(players[0] + " lost the game.")
