import random

class roulette:
	playerList = []
	casinoWinnings = 0
	result = 0
	tableM = 0

	straight_up = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
	first_dozen = [1,2,3,4,5,6,7,8,9,10,11,12]
	second_dozen = [13,14,15,16,17,18,19,20,21,22,23,24]
	third_dozen = [25,26,27,28,29,30,31,32,33,34,35,36]
	first_column = [1,4,7,10,13,16,19,22,25,28,31,43]
	second_column = [2,5,8,11,14,17,20,23,26,29,32,35]
	third_column = [3,6,9,12,15,18,21,24,27,30,33,36]
	lower_half = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
	even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
	red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
	black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
	odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
	upper_half = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
	corner = [[1,2,4,5],[2,3,5,6],[4,5,7,8],[5,6,8,9],[7,8,10,11],[8,9,11,12],[10,11,13,14],[11,12,14,15],[13,14,16,17],[14,15,17,18],[16,17,19,20],[17,18,20,21],[19,20,22,23],[20,21,23,24],[22,23,25,26],[23,24,26,27],[25,26,28,29],[26,27,29,30],[28,29,31,32],[29,30,32,33],[31,32,34,35],[32,33,35,36]]
	street = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30],[31,32,33],[34,35,36]]
	line = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
	split = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] #too many combinations -> generate two numbers
	basket = [0,1,2,3]
	bet_placement1 = {1 : ['1-18', lower_half], 2 : ['even', even], 3 :['red', red], 4 : ['black', black], 5 : ['odd', odd], 6 : ['19-36', upper_half], 7 : ['1st Dozen', first_dozen], 8 :['2nd Dozen', second_dozen], 9 : ['3rd Dozen', third_dozen], 10 : ['1st column', first_column], 11 : ['2nd column',second_column], 12 : ['3rd column', third_column] }
	bet_placement2 = {1: ['line', line], 2 : ['corner', corner], 3 : ['street', street]}
	bet_placement3 = {1 : ['straight up', straight_up], 2 : ["split", split], 3 : ['basket', basket]}

	def tableMin(self, tableMin):
		if tableMin == 3:
			self.tableM = 1000
		elif tableMin == 2:
			self.tableM = 2000
		elif tableMin == 1:
			self.tableM = 3000

	def __init__(self):
		self.playerList = []

	def roll(self):
		self.result = random.choice(self.straight_up)

	def spin_phrase(self):
		#print("The dealer is now spinning the wheel")
		time.sleep(1)
		#print("The ball passes", random.randint(0, 36))
		time.sleep(1)
		#print("It almost lands on", random.randint(0, 36))
		time.sleep(1)
		#print("The ball lands on number", roll(), '\n')
		time.sleep(1)

	def player_bet_balance(player):
		#print("How much would you like to bet?")
		player.balance = player.startingBalance - player.bet
		#print("Player", player.playerNumber, "has", player.startingBalance,"dollars and bets", player.bet, "dollars leaving them with", player.balance)

	'''
	Play type 1 will bet on payouts that only give 1:1, 2:1
	Play type 2 will bet on payouts such as 5:1, 8:1, 11:1
	Play type 3 will bet on payouts such as 11:1, 17:1, 35:1
	'''

	def playRound(self):

		self.roll()
		self.tableMin(self.tableM)
		for p in self.playerList:
			if p.balance < self.tableM:
				p.bet = 0
			elif p.balance >= self.tableM:
				p.bet = random.randint(self.tableM, self.tableM*2)

			p.a = random.randint(1,12)
			p.b = random.randint(1,12)
			p.c = random.randint(1,12)
			p.d = random.randint(1,3)
			p.e = random.randint(1,3)
			p.f = random.randint(1,3)
			p.g = random.randint(0, 5) #line
			p.h = random.randint(0, 21) #corner
			p.i = random.randint(0, 11) #street
			p.j = random.randint(0, 36) #straight up
			p.balance -= p.bet
			self.casinoWinnings += p.bet
			if p.playType == 1:
				#if p.balance < tableMin:
					#print("You no longer have funds to play this game")
				if p.bet <= p.balance/3:
					if p.a in self.bet_placement1:
						if self.result in self.bet_placement1[p.a][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet*2
							##print("Congratualtions", p.playerNumber, " you won on", self.bet_placement1[p.a][0], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1]:
							continue

							##print("Oh no! ", p.playerNumber, " you lost, you now have", p.balance, "dollars")
				elif p.bet > p.balance/3 and p.bet < p.balance/1.5:
					p.bet = p.bet/2
					if p.a in self.bet_placement1 and p.b in self.bet_placement1:
						if self.result in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*4
							##print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement1[p.a][0], "and", self.bet_placement1[p.b][0], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement1[p.a][1] or self.result in self.bet_placement1[p.b][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet*2
							#if self.result in self.bet_placement1[p.a][1]:
								#print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement1[p.a][0], "you now have", p.balance, "dollars")
							#elif self.result in self.bet_placement1[p.b][1]:
								#print("Congratualtions", p.playerNumber," you won on", self.bet_placement1[p.b][0], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1]:
							continue

							#print("Oh no! ", p.playerNumber , " you lost, you now have", p.balance, "dollars")
				elif p.bet >= p.balance/1.5:
					p.bet = p.bet/3
					if p.a in self.bet_placement1 and p.b in self.bet_placement1 and p.c in self.bet_placement1:
						if self.result in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement1[p.a][0], 'and', self.bet_placement1[p.b][0], 'and', self.bet_placement1[p.c][0] ,"you now have", p.balance, "dollars")
						elif self.result in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*4
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						elif self.result in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*4
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						elif self.result in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet*2
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*4
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet*2
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet*2
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
			if p.playType == 2:
				#if p.balance < tableMin:
					#print("You no longer have funds to play this game")
				if p.bet <= p.balance/3:
					if self.bet_placement2[p.d][0] == 'line':
						if self.result in self.bet_placement2[p.d][1][p.g]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.g], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g]:
							continue

							#print("Oh no!", p.playerNumber, " you lost, you now have", p.balance, "dollars")
					elif self.bet_placement2[p.d][0] == 'corner':
						if self.result in self.bet_placement2[p.d][1][p.h]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					elif self.bet_placement2[p.d][0] == 'street':
						if self.result in self.bet_placement2[p.d][1][p.i]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*12
							#print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i]:
							continue

							#print("Oh no!", p.playerNumber, " you lost, you now have", p.balance, "dollars")
				elif p.bet > p.balance/3 and p.bet < p.balance/1.5:
					p.bet = p.bet/2
					if self.bet_placement2[p.d][0] == 'line':
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*15
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.g], "and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							continue

							#print("Oh no!", p.playerNumber, " you lost, you now have", p.balance, "dollars")
					elif self.bet_placement2[p.d][0] == 'corner':
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*21
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.h], "and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*12
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[3][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					elif self.bet_placement2[p.d][0] == 'street':
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*18
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.g], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*12
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
				elif p.bet >= p.balance/1.5:
					p.bet = p.bet/3
					if self.bet_placement2[p.d][0] == 'line':
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*27
							self.casinoWinnings -= p.bet*27
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.g], "and", self.bet_placement2[2][1][p.h], "and", self.bet_placement2[3][1][p.i],  "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*21
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*18
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*12
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.g], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*15
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[2][1][p.h], "and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					elif self.bet_placement2[p.d][0] == 'corner':
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*27
							self.casinoWinnings -= p.bet*27
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.h], "and", self.bet_placement2[3][1][p.i], "and", self.bet_placement2[1][1][p.g],  "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*15
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*21
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*18
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[3][1][p.i], "and", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*12
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'street':
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*27
							self.casinoWinnings -= p.bet*27
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.h], "and", self.bet_placement2[1][1][p.g], "and", self.bet_placement2[2][1][p.g],  "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*18
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*15
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*21
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*12
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							continue

							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
			if p.playType == 3:
				if p.bet <= p.balance/3:
					if self.result == self.bet_placement3[1][1][p.j]:
						p.balance += p.bet*36
						self.casinoWinnings -= p.bet*36
						#print("Wow", p.playerNumber," that is amazing you got the number!", self.bet_placement3[1][1][p.j], "you now have", p.balance, "dollars")
					if self.result != self.bet_placement3[1][1][p.j]:
						continue

						#print("Oh no!", p.playerNumber,"", self.result, "did not land on", self.bet_placement3[1][1][p.j], "you now have", p.balance, "dollars")
				elif p.bet > p.balance/3 and p.bet < p.balance/1.5:
					y = self.bet_placement3[1][1][p.j]
					z = []
					if y == 36:
						z.append(35)
						z.append(36)
					elif y == 0:
						z.append(0)
						z.append(1)
					else:
						z.append(y)
						z.append(y+1)
					if self.result in z:
						p.balance += p.bet*18
						self.casinoWinnings -= p.bet*18
						#print("Wow", p.playerNumber," that is amazing, you got it, lucky pairing!", self.result, "is in", z, "you now have", p.balance, "dollars")
					if self.result not in z:
						continue

						#print("Oh no!", p.playerNumber, self.result, "did not land in", z, "you now have", p.balance, "dollars")
				elif p.bet >= p.balance/1.5:
					p.bet = p.bet/2
					if self.result == self.bet_placement3[1][1][p.j] and self.result in self.bet_placement3[3][1]:
						p.balance += p.bet*48 #The most a player can make in one round
						self.casinoWinnings -= p.bet*48
						#print("Wow", p.playerNumber," that is amazing you got both!", self.result, "is in", self.bet_placement3[1][1][p.j], "and", self.bet_placement3[3][1], "you now have", p.balance, "dollars")
					elif self.result == self.bet_placement3[1][1][p.j] and self.result not in self.bet_placement3[3][1]:
						p.balance += p.bet*36
						self.casinoWinnings -= p.bet*36
						#print("Wow", p.playerNumber," that is amazing you got the number!", self.bet_placement3[1][1][p.j], "you now have", p.balance, "dollars")
					elif self.result != self.bet_placement3[1][1][p.j] and self.result in self.bet_placement3[3][1]:
						p.balance += p.bet*12
						self.casinoWinnings -= p.bet*12
						#print("Wow", p.playerNumber," that is amazing you got the basket!", self.bet_placement3[3][1], "you now have", p.balance, "dollars")
					elif self.result != self.bet_placement3[1][1][p.j] and self.result not in self.bet_placement3[3][1]:
						continue

						#print("Oh no!", p.playerNumber,"", self.result, "did not land in", self.bet_placement3[1][1][p.j], "or", self.bet_placement3[3][1], "you now have", p.balance, "dollars")
		#print(self.casinoWinnings)
			#player_bet_balance(p)
			#bet_places(p)
