import random, time

tableMin = 1000 #need to delete later and only use tableMin from Roulette class

class player:
	global a, b, c, d, e, f, g, h, i, j
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	f = 0
	g = 0
	h = 0
	i = 0
	j = 0
	balance = 0
	playType = 0
	startingBalance = 0
	bet = 0


	def __init__(self, num, startingBalance):
		self.playerNumber = num
		self.startingBalance = startingBalance
		self.balance = self.balance
		self.playType = random.randint(1,3)
		self.bet = random.randint(tableMin, startingBalance)
		self.a = random.randint(1,12)
		self.b = random.randint(1,12)
		self.c = random.randint(1,12)
		self.d = random.randint(1,3)
		self.e = random.randint(1,3)
		self.f = random.randint(1,3)
		self.g = random.randint(0, 5) #line
		self.h = random.randint(0, 3) #corner
		self.i = random.randint(0, 11) #street
		self.j = random.randint(0, 36) #straight up

p1 = player(1, 1000)
p2 = player(2, 1500)
p3 = player(3, 2000)
p4 = player(4, 2500)
p5 = player(5, 3000)
p6 = player(6, 3500)

pL = [p1, p2, p3, p4, p5, p6]


class rouletteGame:
	playerList = []
	casinoWinnings = 0
	result = 0
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
	corner = [[1,2,4,5],[2,3,5,6],[4,5,7,8],[5,6,8,9]]
	street = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30],[31,32,33],[34,35,36]]
	line = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
	split = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] #too many combinations -> generate two numbers
	basket = [0,1,2,3]
	bet_placement1 = {1 : ['1-18', lower_half], 2 : ['even', even], 3 :['red', red], 4 : ['black', black], 5 : ['odd', odd], 6 : ['19-36', upper_half], 7 : ['1st Dozen', first_dozen], 8 :['2nd Dozen', second_dozen], 9 : ['3rd Dozen', third_dozen], 10 : ['1st column', first_column], 11 : ['2nd column',second_column], 12 : ['3rd column', third_column] }
	bet_placement2 = {1: ['line', line], 2 : ['corner', corner], 3 : ['street', street]}
	bet_placement3 = {1 : ['straight up', straight_up], 2 : ["split", split], 3 : ['basket', basket]}

	'''
	def tableMin(self, tableMin):
		if tableMin == 1:
			tableMin = 1000
		elif tableMin == 2:
			tableMin = 2000
		elif tableMin == 3:
			tableMin = 3000
	'''
	def __init__(self, pL):
		self.playerList = pL

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


	def playGame(self):

		self.roll()
		for p in self.playerList:
			p.balance = p.startingBalance - p.bet
			'''
			if p.playType == 1:
				if p.bet <= p.startingBalance/3:
					#print("Player", p.playerNumber, "places their bet on", self.bet_placement1[p.a][0])
				elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.5:
					#print("Player", p.playerNumber, "places their bet on", self.bet_placement1[p.a][0] + " and " + self.bet_placement1[p.b][0])
				elif p.bet >= p.startingBalance/1.5:
					#print("Player", p.playerNumber, "places their bet on", self.bet_placement1[p.a][0] + ", " + self.bet_placement1[p.b][0], "and", self.bet_placement1[p.c][0])
			elif p.playType == 2:
				if self.bet_placement2[p.d][0] == 'line':
					if p.bet <= p.startingBalance/3:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.g])
					elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.5:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.g], " and ",  self.bet_placement2[2][1][p.h])
					elif p.bet >= p.startingBalance/1.5:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.g], ", ", self.bet_placement2[2][1][p.h], "and", self.bet_placement2[3][1][p.i])
				elif self.bet_placement2[p.d][0] == 'corner':
					if p.bet <= p.startingBalance/3:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.h])
					elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.5:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.h], " and ",  self.bet_placement2[3][1][p.i])
					elif p.bet >= p.startingBalance/1.5:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.h], ", ", self.bet_placement2[3][1][p.i], "and", self.bet_placement2[1][1][p.g])
				elif self.bet_placement2[p.d][0] == 'street':
					if p.bet <= p.startingBalance/3:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.i])
					elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.5:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.i], " and ",  self.bet_placement2[1][1][p.g])
					elif p.bet >= p.startingBalance/1.5:
						#print("Player", p.playerNumber, "places their bet on", self.bet_placement2[p.d][1][p.i], ", ", self.bet_placement2[1][1][p.g], "and", self.bet_placement2[2][1][p.h])
			elif p.playType == 3:
				if p.bet <= p.startingBalance/3:
					#print("Player", p.playerNumber, "places their bet on", self.bet_placement3[1][1][p.j])
				elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.3:
					#print("Player", p.playerNumber, "places their bet on", self.bet_placement3[2][0])
				elif p.bet >= p.startingBalance/3:
					#print("Player", p.playerNumber, "places their bet on", self.bet_placement3[1][1][p.j], ", ", self.bet_placement3[3][1])
			'''
			if p.playType == 1:
				#if p.startingBalance < tableMin:
					#print("You no longer have funds to play this game")
				if p.bet <= p.startingBalance/3:
					if p.a in self.bet_placement1:
						if self.result in self.bet_placement1[p.a][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							##print("Congratualtions", p.playerNumber, " you won on", self.bet_placement1[p.a][0], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement1[p.a][1]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							##print("Oh no! ", p.playerNumber, " you lost, you now have", p.balance, "dollars")
				elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.5:
					if p.a in self.bet_placement1 and p.b in self.bet_placement1:
						if self.result in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet
							##print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement1[p.a][0], "and", self.bet_placement1[p.b][0], "you now have", p.balance, "dollars")
						elif self.result in self.bet_placement1[p.a][1] or self.result in self.bet_placement1[p.b][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet*2
							#if self.result in self.bet_placement1[p.a][1]:
								#print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement1[p.a][0], "you now have", p.balance, "dollars")
							#elif self.result in self.bet_placement1[p.b][1]:
								#print("Congratualtions", p.playerNumber," you won on", self.bet_placement1[p.b][0], "you now have", p.balance, "dollars")
						elif self.result not in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no! ", p.playerNumber , " you lost, you now have", p.balance, "dollars")
				elif p.bet >= p.startingBalance/1.5:
					if p.a in self.bet_placement1 and p.b in self.bet_placement1 and p.c in self.bet_placement1:
						if self.result in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement1[p.a][0], 'and', self.bet_placement1[p.b][0], 'and', self.bet_placement1[p.c][0] ,"you now have", p.balance, "dollars")
						if self.result in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*2
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						if self.result in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*2
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						if self.result in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance += p.bet*4
							self.casinoWinnings -= p.bet*2
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						if self.result not in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						if self.result not in self.bet_placement1[p.a][1] and self.result in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						if self.result not in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result in self.bet_placement1[p.c][1]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							#print("Congratualtions ", p.playerNumber, " you won! you now have", p.balance, "dollars")
						if self.result not in self.bet_placement1[p.a][1] and self.result not in self.bet_placement1[p.b][1] and self.result not in self.bet_placement1[p.c][1]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
			if p.playType == 2:
				#if p.startingBalance < tableMin:
					#print("You no longer have funds to play this game")
				if p.bet <= p.startingBalance/3:
					if self.bet_placement2[p.d][0] == 'line':
						if self.result in self.bet_placement2[p.d][1][p.g]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							#print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.g], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber, " you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'corner':
						if self.result in self.bet_placement2[p.d][1][p.h]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'street':
						if self.result in self.bet_placement2[p.d][1][p.i]:
							p.balance += p.bet*2
							self.casinoWinnings -= p.bet
							#print("Congratualtions ", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber, " you lost, you now have", p.balance, "dollars")
				elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.5:
					if self.bet_placement2[p.d][0] == 'line':
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.g], "and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*3
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*4.5
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber, " you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'corner':
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*10.5
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.h], "and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*4.5
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[p.d][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber, " you won on", self.bet_placement2[3][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'street':
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.g], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*3
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
				elif p.bet >= p.startingBalance/1.5:
					if self.bet_placement2[p.d][0] == 'line':
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*27
							self.casinoWinnings -= p.bet*13.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.g], "and", self.bet_placement2[2][1][p.h], "and", self.bet_placement2[3][1][p.i],  "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*10.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.g], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*7.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[2][1][p.h], "and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g] and self.result in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*4.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result in self.bet_placement2[3][1][p.i]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*3
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.g] and self.result not in self.bet_placement2[2][1][p.h] and self.result not in self.bet_placement2[3][1][p.i]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'corner':
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*27
							self.casinoWinnings -= p.bet*13.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.h], "and", self.bet_placement2[3][1][p.i], "and", self.bet_placement2[1][1][p.g],  "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*7.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*10.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*4.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[3][1][p.i], "and", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h] and self.result in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*3
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[3][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result in self.bet_placement2[1][1][p.g]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.h] and self.result not in self.bet_placement2[3][1][p.i] and self.result not in self.bet_placement2[1][1][p.g]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
					if self.bet_placement2[p.d][0] == 'street':
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*27
							self.casinoWinnings -= p.bet*13.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.h], "and", self.bet_placement2[1][1][p.g], "and", self.bet_placement2[2][1][p.g],  "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*18
							self.casinoWinnings -= p.bet*9
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*15
							self.casinoWinnings -= p.bet*7.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i],"and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*6
							self.casinoWinnings -= p.bet*3
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[p.d][1][p.i], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*21
							self.casinoWinnings -= p.bet*10.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "and", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i] and self.result in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*12
							self.casinoWinnings -= p.bet*6
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[1][1][p.g], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result in self.bet_placement2[2][1][p.h]:
							p.balance += p.bet*9
							self.casinoWinnings -= p.bet*4.5
							#print("Congratualtions", p.playerNumber," you won on", self.bet_placement2[2][1][p.h], "you now have", p.balance, "dollars")
						if self.result not in self.bet_placement2[p.d][1][p.i] and self.result not in self.bet_placement2[1][1][p.g] and self.result not in self.bet_placement2[2][1][p.h]:
							p.balance = p.balance
							self.casinoWinnings += p.bet
							#print("Oh no!", p.playerNumber," you lost, you now have", p.balance, "dollars")
			if p.playType == 3:
				if p.bet <= p.startingBalance/3:
					if self.result == self.bet_placement3[1][1][p.j]:
						p.balance += p.bet*37
						#print("Wow", p.playerNumber," that is amazing you got the number!", self.bet_placement3[1][1][p.j], "you now have", p.balance, "dollars")
					if self.result != self.bet_placement3[1][1][p.j]:
						p.balance = p.balance
						self.casinoWinnings += p.bet
						#print("Oh no!", p.playerNumber,"", self.result, "did not land on", self.bet_placement3[1][1][p.j], "you now have", p.balance, "dollars")
				elif p.bet > p.startingBalance/3 and p.bet < p.startingBalance/1.3:
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
						self.casinoWinnings -= p.bet*9
						#print("Wow", p.playerNumber," that is amazing, you got it, lucky pairing!", self.result, "is in", z, "you now have", p.balance, "dollars")
					if self.result not in z:
						p.balance = p.balance
						self.casinoWinnings += p.bet
						#print("Oh no!", p.playerNumber, self.result, "did not land in", z, "you now have", p.balance, "dollars")
				elif p.bet >= p.startingBalance/3:
					if self.result == self.bet_placement3[1][1][p.j] and self.result in self.bet_placement3[3][1]:
						p.balance += p.bet*48 #The most a player can make in one round
						self.casinoWinnings -= p.bet*24
						#print("Wow", p.playerNumber," that is amazing you got both!", self.result, "is in", self.bet_placement3[1][1][p.j], "and", self.bet_placement3[3][1], "you now have", p.balance, "dollars")
					if self.result == self.bet_placement3[1][1][p.j] and self.result not in self.bet_placement3[3][1]:
						p.balance += p.bet*36
						self.casinoWinnings -= p.bet*18
						#print("Wow", p.playerNumber," that is amazing you got the number!", self.bet_placement3[1][1][p.j], "you now have", p.balance, "dollars")
					if self.result != self.bet_placement3[1][1][p.j] and self.result in self.bet_placement3[3][1]:
						p.balance += p.bet*18
						self.casinoWinnings -= p.bet*9
						#print("Wow", p.playerNumber," that is amazing you got the basket!", self.bet_placement3[3][1], "you now have", p.balance, "dollars")
					if self.result != self.bet_placement3[1][1][p.j] and self.result not in self.bet_placement3[3][1]:
						p.balance = p.balance
						self.casinoWinnings += p.bet
						#print("Oh no!", p.playerNumber,"", self.result, "did not land in", self.bet_placement3[1][1][p.j], "or", self.bet_placement3[3][1], "you now have", p.balance, "dollars")
		print(self.casinoWinnings)
			#player_bet_balance(p)
			#bet_places(p)

newGame = rouletteGame(pL)
newGame.playGame()

'''
player_bet_balance(p1)
player_bet_balance(p2)
player_bet_balance(p3)
player_bet_balance(p4)
player_bet_balance(p5)
player_bet_balance(p6)

bet_places(p1)
bet_places(p2)
bet_places(p3)
bet_places(p4)
bet_places(p5)
bet_places(p6)

spin_phrase()

bet(p1)
bet(p2)
bet(p3)
bet(p4)
bet(p5)
bet(p6)
'''
