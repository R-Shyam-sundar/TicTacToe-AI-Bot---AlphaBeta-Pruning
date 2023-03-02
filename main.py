'''
	Name: R.Shyam Sundar
	Roll: CS20B1029
	Date: 02/02/2023
	AI - Lab
	Alpha-Beta Pruning on Tic-Tac-Toe Game - Game Tree
'''

class Tic_tac_toe:
	def __init__(self):
		self.print_rules()
		self.board = [['*',"*","*"],["*","*","*"],["*","*","*"]]
		self.moves = 0
		self.print_board()	
		self.start()
		pass

	def print_rules(self):
		print("Welcome to Tic-Tac-Toe Game");
		print("The rules of the game are as follows: ")
		print("1. The coordinates in this game are 0-indexed")
		print("2. The program plays with character 'O' and you play with character 'X'")
		print("3. At each turn type two space separated integers denoting the coordinates in which you play 'X'")
		print("4. The coordinates")
		for i in range(0,3):
			print("|",end="")
			for j in range(0,3):
				print(f"{i,j}",end="|")
			print("",end="\n")
		pass

	def print_board(self):
		print("The Board: ")
		for i in range(0,3):
			print("|",end="")
			for j in range(0,3):
				print(f"{self.board[i][j]}",end="|")
			print("",end="\n")
		print(f"MOVES COUNT : [{self.moves} moves completed]")
		pass

	def start(self):
		choice = 3;
		while choice<1 or choice>2:
			choice = int(input("You start the game: 1\nComputer Starts the game: 2\nYour choice : "))
			if(choice<1 or choice>2):
				print("ERROR: Enter a valid choice")
				pass
			pass
		if choice == 1:
			self.opponent()
		else:
			self.myself()
		pass

	def opponent_move(self,move):
		mn = 1000
		x = -1
		y = -1
		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == '*':
					self.board[i][j] = 'X'
					val = computer_move(move+1)
					if val<mn:
						mn = val
						x = i
						y = j
					self.board[i][j] = '*'
		return x,y
		pass
	
	def computer_move(self,move):
		if move == 9:
			res = self.check_win()
			if res == 3:
				return 1
			elif res == 1:
				return 0
			else:
				return -1
		mx = -1000
		x = -1
		y = -1
		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == '*':
					self.board[i][j] = 'O'
					val = opponent_move(move+1)
					if val>mx:
						mx = val
						x = i
						y = j
					self.board[i][j] = '*'
		return x,y
		pass

	def myself(self):
		# Apply Alpha-Beta Pruning to find the optimal value
		x,y = self.computer_move(self.moves)
		self.moves += 1

		pass

	def opponent(self):
		self.moves += 1
		print("Enter the coordinates (space separated):  ",end="")
		x,y = map(int,input().split())
		while self.board[x][y] == '*':
			if x<0 or x>2 or y<0 or y>2:
				print("ERROR: Enter valid coordinates")
			elif self.board[x][y] != '*':
				print("ERROR: Enter a valid choice")
			else:
				self.board[x][y] = 'X'
				break
		self.print_board()
		res = self.check_win()
		if res == 0: #game in progress 
			self.myself()
		elif res == 1: #game ended in draw
			print("RESULT: The Game has ended in DRAW")
		elif res == 2: #opponent won the game
			print("RESULT: Congratulations you won the game")
		elif res == 3: #computer won the game
			print("RESULT: Computer has won the game")
		pass

	def check_win(self):
		#Game is still in progress
		if self.moves < 9:
			return 0
		
		#Check if 'X' won the game
		for j in range(0,3):
			cnt_col = 0
			cnt_row = 0
			for i in range(0,3):
				if self.board[i][j] == 'X':
					cnt_col += 1
				if self.board[j][i] == 'X':
					cnt_row += 1
			if cnt_row==3 or cnt_col==3:
				return 2;
		
		cnt_d1 = 0
		cnt_d2 = 0
		for i in range(0,3):
			if self.board[i][i] == 'X':
				cnt_d1 += 1
			if self.board[i][2-i] == 'X':
				cnt_d2 += 1
		if cnt_d1==3 or cnt_d2==3:
			return 2

		#Check if 'O' won the game
		for j in range(0,3):
			cnt_col = 0
			cnt_row = 0
			for i in range(0,3):
				if self.board[i][j] == 'O':
					cnt_col += 1
				if self.board[j][i] == 'O':
					cnt_row += 1
			if cnt_row==3 or cnt_col==3:
				return 3;

		cnt_d1 = 0
		cnt_d2 = 0
		for i in range(0,3):
			if self.board[i][i] == 'O':
				cnt_d1 += 1
			if self.board[i][2-i] == 'O':
				cnt_d2 += 1
		if cnt_d1==3 or cnt_d2==3:
			return 3

		#Game ended in a draw
		return 1


def main():
	GT = Tic_tac_toe()
	pass

if __name__ == '__main__':
	main()
