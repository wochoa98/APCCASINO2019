class blackjackGame:


	def __init__(self, bjNumIn, DH2In):
		self.bjNumIn = bjNum
		self.DH2In = DH2
		self.playerList = playerList[]
	

	import random
	
	deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	blackjackWinnings = 0
	bjTempPot = 50000

	class player:

		startingBalance = 1000
		balance = 1000
		plusMinus = 0
		playType = 0
		toat = 0
		final = 0
		win = 0
		#winCount=0
		hand = []
		#count = 0

		def dealStart(self):
			self.hand = []
			for i in range(2):
				card = random.choice(deck)
				self.hand.append(card)
			
		def __init__(self, countIn):
			self.count=countIn
			self.playType=random.randint(1, 3)
		
		def total(self):
			for i in self.hand:
				if i == 'A' and self.toat<=10:
					self.toat+=11
				elif i == 'A' and self.toat>=11:
					self.toat+=1
				else:
					self.toat+=i


	dealer0 = dealer()

	def takeBets():
		for i in playerList:
			i.balance = i.balance - 10
			bjTempPot += 10
	
	def payout():
		for i in playerList:
			if i.win == 3:
				i.balance = i.balance + 25
				bjTempPot = bjTempPot - 25
			elif i.win == 2:
				i.balance = i.balance + 10
				bjTempPot = bjTempPot -10
			elif i.win == 1:
				i.balance = i.balance + 20
				bjTempPot = bjTempPot - 20

	def dealHand():
		for i in playerList:
			i.dealStart()
		dealer0.dealStart()


	def play(i):
		if i.playType == 1:
			i.total()
			done = 1
			if i.toat == bjNum:
				i.final = i.toat
				i.win = 3
				done = 0
			while(done):
				if i.toat >= 0 and i.toat <= 14:
					card = random.choice(deck)
					i.hand.append(card)
					i.total()
				elif i.toat >= 15 and i.toat <= 16:
					hit = random.randint(0, 1)
					if hit == 0:
						i.final=i.toat
						done = 0
					elif hit == 1:
						card = random.choice(deck)
                               			i.hand.append(card)
						i.total()
				elif i.toat >= 17 and i.toat <= bjNum:
					i.final = i.toat
					done = 0
				elif i.toat > bjNum:
					i.final = -1
					done = 0
		elif i.playType == 2:
			i.total()
			done = 1
                	if i.toat == bjNum:
                        	i.final = i.toat
				i.win = 3
                        	done = 0
                	while(done):
                        	if i.toat >= 0 and i.toat <= 11:
                                	card = random.choice(deck)
                                	i.hand.append(card)
                                	i.total()
                        	elif i.toat >= 11 and i.toat <= 15:
                                	hit = random.randint(0, 3)
                                	if hit < 1:
						i.final = i.toat
                                        	done = 0
                                	elif hit >= 1:
                                        	card = random.choice(deck)
                                        	i.hand.append(card)
						i.total()
                        	elif i.toat >= 15 and i.toat <= bjNum:
                                	i.final = i.toat
                                	done = 0
                        	elif i.toat > bjNum:
                                	i.final = -1
                                	done = 0
		elif i.playType == 3:
			i.total()
			done = 1
                	if i.toat == bjNum:
                        	i.final = i.toat
				i.win = 3
                        	done = 0
                	while(done):
                        	if i.toat >= 0 and i.toat <= 11:
                                	card = random.choice(deck)
                                	i.hand.append(card)
                                	i.total()
                        	elif i.toat >= 11 and i.toat <= 13:
                                	hit = random.randint(0, 8)
                                	if hit < 1:
						i.final = i.toat
                                        	done = 0
                                	elif hit >= 1:
                                        	card = random.choice(deck)
                                        	i.hand.append(card)
						i.total()
                        	elif i.toat >= 13 and i.toat <= bjNum:
                                	i.final = i.toat
                                	done = 0
                        	elif i.toat > bjNum:
                                	i.final = -1
                                	done = 0
	def playDealer(dealer):
		if dealer.playType == 4:
			dealer.total()
			done = 1
			if dealer.toat == bjNum:
				dealer.final = dealer.toat
				done = 0
			while(done):
				if dealer.toat >=0 and dealer.toat < DH2:
					card = random.choice(deck)
					dealer.hand.append(card)
					dealer.total()
				elif dealer.toat >= DH2 and dealer.toat <= bjNum:
					dealer.final = dealer.toat
					done = 0
				elif dealer.toat > bjNum:
					dealer.final = -1
					done = 0

	def blackjackgame():
		#playerNum = 0
		#playerNum = input('How many players would you like to use?: ')
		done = 1
		#idk=2
		#for i in range(playerNum):
		#	newPlayer = player(idk)
		#	playerList.append(newPlayer)
		#	idk+=1
		while(done):
			choice = 1
			#print('Press 1 to play a round of blackjack.')
			#print('Press 2 to quit.')
			#choice = input('Choice: ')
			ntb = 0
			if choice == 1:
				takeBets()
				dealHand()
				for i in playerList:
					play(i)
				playDealer(dealer0)
				dealer0.final = ntb
				for i in playerList:
					if i.win = 0:
						if i.final == ntb:
							i.win = 2
						elif i.final > ntb:
							i.win = 1
						elif i.final < ntb:
							i.win = 0
				payout()
				for i in playerList:
					i.toat=0
					i.final=0
					i.win=0
					i.hand=[]
				dealer0.toat=0
				dealer0.final=0
				dealer0.win=0
				dealer0.hand=[]
				done = 0
			#elif choice == 2:
				#done = 0
				#for i in playerList:
				#	print("Player ", i.count, " won this many times: ", i.winCount)
			#else:
				#print('Invalid entry, please enter 1 or 2.')
	blackjackgame()

class dealer:

	playType = 4
        toat = 0
        final = 0
        win = 0
        winCount=0
        hand = []
        count = 0

        def dealStart(self):
        	self.hand = []
                for i in range(2):
                	card = random.choice(deck)
                        self.hand.append(card)


        def total(self):
                for i in self.hand:
                	if i == 'A' and self.toat<=10:
                        	self.toat+=11
                        elif i == 'A' and self.toat>=11:
                                self.toat+=1
                        else:
                                self.toat+=i
