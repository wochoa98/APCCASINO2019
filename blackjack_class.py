class blackjackGame:


	def __init__(self):
		self.bjNum = 21
		self.DH2 = 16
		self.playerList = playerList[]
		self.dealer0 = dealer()

	import random
	
	deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	bjTempPot = 50000


	def takeBets():
		for i in playerList:
			i.balance = i.balance - 1000
			bjTempPot += 1000
	
	def payout():
		for i in playerList:
			if i.win == 3:
				i.balance = i.balance + 2500
				bjTempPot = bjTempPot - 2500
			elif i.win == 2:
				i.balance = i.balance + 1000
				bjTempPot = bjTempPot -1000
			elif i.win == 1:
				i.balance = i.balance + 2000
				bjTempPot = bjTempPot - 2000

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
		done = 1
		while(done):
			choice = 1
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
				bjWinnings = bjTempPot - 50000
				done = 0

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
