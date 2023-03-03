'''
	Name: R.Shyam Sundar
	Roll: CS20B1029
	Date: 02/02/2023
	AI - Lab
	Alpha-Beta Pruning on Tic-Tac-Toe Game - Game Tree
'''

import sys

sys.setrecursionlimit(1500)

class Tic_tac_toe:
	def __init__(self):
		self.print_rules()
		self.board = [['*',"*","*"],["*","*","*"],["*","*","*"]]
		self.moves = 0
		self.print_board()	
		self.start()
		self.computer_move_cnt = 0
		self.opponent_move_cnt = 0
		pass

	def print_rules(self):
		print("\nWelcome to Tic-Tac-Toe Game");
		print("The rules of the game are as follows: ")
		print("1. The coordinates in this game are 0-indexed")
		print("2. The program plays with character 'O' and you play with character 'X'")
		print("3. At each turn type two space separated integers denoting the coordinates in which you play 'X'\n")
		for i in range(0,3):
			print("|",end="")
			for j in range(0,3):
				print(f"{i,j}",end="|")
			print("",end="\n")
		pass

	def print_board(self):
		print("\nThe Board: ")
		for i in range(0,3):
			print("|",end="")
			for j in range(0,3):
				print(f"{self.board[i][j]}",end="|")
			print("",end="\n")
		print(f"\nMOVES COUNT : [{self.moves} moves completed]")
		pass

	def start(self):
		choice = 3;
		while choice<1 or choice>2:
			choice = int(input("\nYou start the game: 1\nComputer Starts the game: 2\n\nYour choice : "))
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
		res = self.check_win()
		if res == 3:
			return 1
		elif res == 1:
			return 0
		elif res == 2:
			return -1
		mn = 1000
		x = -1
		y = -1
		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == '*':
					self.board[i][j] = 'X'
					val,tx,ty = self.computer_move(move+1)
					if val<mn:
						mn = val
						x = i
						y = j
					self.board[i][j] = '*'
		return mn
		pass
	
	def computer_move(self,move):
		res = self.check_win()
		if res == 3:
			return 1,-1,-1
		elif res == 1:
			return 0,-1,-1
		elif res == 2:
			return -1,-1,-1
		mx = -1000
		x = -1
		y = -1
		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == '*':
					self.board[i][j] = 'O'
					val = self.opponent_move(move+1)
					if val>mx:
						mx = val
						x = i
						y = j
					self.board[i][j] = '*'
		return mx,x,y
		pass

	def myself(self):
		# Apply Alpha-Beta Pruning to find the optimal value
		res = self.check_win()
		if res == 1: #game ended in draw
			print("RESULT: The Game has ended in DRAW")
			return
		elif res == 2: #opponent won the game
			print("RESULT: Congratulations you won the game")
			return
		elif res == 3: #computer won the game
			print("RESULT: Computer has won the game")
			return
		val,x,y = self.computer_move(self.moves)
		self.moves += 1
		self.board[x][y] = 'O'
		self.print_board()
		self.opponent()
		pass

	def opponent(self):
		res = self.check_win()
		if res == 1: #game ended in draw
			print("RESULT: The Game has ended in DRAW")
			return
		elif res == 2: #opponent won the game
			print("RESULT: Congratulations you won the game")
			return
		elif res == 3: #computer won the game
			print("RESULT: Computer has won the game")
			return
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
		self.myself()
		pass

	def check_win(self):
		
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

		if self.moves < 9:     #Game in progress
			return 0
		else:                  #Game ended in a draw
			return 1


def main():
	GT = Tic_tac_toe()
	pass

if __name__ == '__main__':
	main()
