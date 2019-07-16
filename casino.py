import random
from array import *

class casino:
	profit = 0
	poker = 0
	blackjack = 0
	fish = 0
	roulette = 0
	horses = 0
	rounds = 0
	quit = 0


        def simMenu(self):
                self.poker = input("Do you want to run Poker? Yes[1]/No[0]: ")
                if self.poker == 1:
                        self.pokerGame = poker()
                        pokerVig = input("What would you like the rake percent to be (write as decimal): ")
                        pokerGame.rake = pokerVig
                self.blackjack = input("Do you want to run Blackjack? Yes[1]/No[0]: ")
                if self.blackjack == 1:
                        self.blackjackGame = blackjack()
                        stand = input("What is the dealer's hard stand value (Recommended 17): ")
                        # set stand to 17 in blackjack
                self.fish = input("Do you want to run Go Fish? Yes[1]/No[0]: ")
                if self.fish == 1:
			self.fishGame = goFish()
                        fishVig = input("What would you like the rake percent to be (write as decimal): ")
                        self.fishGame.vig = fishVig
                        buyIn = input("Do you want a high table minimum [1], an average table minimum [2], or a low table minimum [3]?: ")
                        #set fishGame.tableMin = buyIn
                self.roulette = input("Do you want to run roulette? Yes[1]/No[0]: ")
                if self.roulette == 1:
			self.rouletteGame = roulette()
                        tableMin = input("Do you want a high table minimum [1], an average table minimum [2], or a low table minimum [3]?: ")
                        #set variable in game
                self.horses = input("Do you want to run horse betting? Yes[1]/No[0]: ")
                if self.horses == 1:
			self.horseBetting = horses()
                        accuracy = input("Do you want the horse odd predictions to be very accurate [1], somewhat accurate [2], or innaccurate [3]: ")
                        #set variable in game
                self.rounds = input("How many rounds would you like to run through?: ")


	def __init__(self):
		self.customers = [] #will be list of all active customers
		self.leaderboard = [] #will be static, holds player records whether active in casino or not
		self.custCount = len(self.customers)
		#set up games
		self.simMenu()
		#for initial start, 30 people enter
		for i in range(30):
			newPlayer = player(self.custCount) #custCount is length of the list, so the current number before the add is the desired index
			if self.custCount < 6: #first 6 players go to poker
				newPlayer.status = "Poker"
				self.pokerGame.playerList.append(newPlayer)
			elif self.custCount >= 6 and self.custCount < 12: #second group of 6 play blackjack
				newPlayer.status = "Blackjack"
				self.blackjackGame.playerList.append(newPlayer)
			elif self.custCount >=12 and self.custCount < 18: #third group of 6 plays Go Fish
				newPlayer.status = "Go Fish"
				self.fishGame.playerList.append(newPlayer)
			elif self.cutCount >=18 and self.custCount < 24: #fourth group of 6 plays Roulette
				newPlayer.status = "Roulette"
				self.rouletteGame.playerList.append(newPlayer)
			else: #fifth group of 6 to horse betting
				newPlayer.status = "Horse Betting"
				self.borseBetting.playerList.append(newPlayer)
                        self.customers.append(newPlayer) #added as active player
                        self.leaderboard.append(newPlayer) #added to records		

	def playerControl(self):
		# run a check first for players that will not make minimums, check poker for struggling people who are being outbet, readd new players to fill void
		#make minimum money at a poker table 5k, every other game minimum is 1k, players leave their games if they have less than 1k at start of round
		#check poker first for 5k
		for players in self.pokerGame.playerList:
			if players.balance < 5000: 
				self.pokerGame.playerList.remove(players) #removes from players and active customers, keeps record
				self.customers.remove(players)
				for people in self.leaderboard:
					if people == players:
						people.status == "OOH"
				newPlayer = player(self.custCount)
				newPlayer.status = "Poker"
				self.customers.append(newPlayer)
				self.leaderboard.append(newPlayer)
				self.pokerGame.playerList.append(newPlayer)
		#check each game for less than 1000 now
		for players in self.blackjackGame.playerList:
			if players.balance < 1000:
				self.blackjackGame.playerList.remove(players)
				self.customers.remove(players)
				for people in self.leaderboard:
					if people == players:
						people.status = "OOH"
				newPlayer = player(self.custCount)
				newPlayer.status = "Blackjack"
				self.customers.append(newPlayer)
				self.leaderboard.append(newPlayer)
				self.blackjackGame.playerList.append(newPlayer)
		for players in self.fishGame.playerList:
			if players.balance < 1000:
				self.fishGame.playerList.remove(players)
				self.customers.remove(players)
				for people in self.leaderboard:
					if people == players:
						people.status = "OOH"
				newPlayer = player(custCount)
				newPlayer.status = "Go Fish"
				self.customers.append(newPlayer)
				self.leaderboard.append(newPlayer)
				self.fishGame.payerList.append(newPlayer)
		for players in self.rouletteGame.playerList:
			if players.balance < 1000:
				self.rouletteGame.playerList.remove(players)
				self.customers.remove(players)
				for people in self.leaderboard:
					if people == players:
						people.status == "OOH"
				newPlayer = player(custCount)
				newPlayer.status = "Roulette"
				self.customers.append(newPlayer)
				self.leaderboard.append(newPlayer)
				self.rouletteGame.playerList.append(newPlayer)
		for players in self.horseBetting.playerList:
			if players.balance < 1000:
				self.horseBetting.playerList.remove(players)
				self.customers.remove(players)
				for people in self.leaderboard:
					if people == players:
						people.status == "OOH"
				newPlayer = player(custCount)
				newPlayer.status = "Horse Betting"
				self.customers.append(newPlayer)
				self.leaderboard.append(newPlayer)
				self.horseBetting.playerList.append(newPlayer)
		playerAction = random.randint(1,4) # 1=addPlayer, 2=deletePlayer, 3=movePlayer, 4=noChange
		if playerAction == 1:
			player2add = player(custCount)
			gameAdded = random.randint(1,5) #selects game randomly that it will append to
			if gameAdded == 1: # 1 will be poker
				player2add.status = "Poker"
				#self.pokerGame.playerList.append(player2add) #added to poker player list
			elif gameAdded == 2: # 2 will be blackjack
				player2add.status = "Blackjack"
				#self.blackjackGame.playerList.append(player2add) #added to blackjack player list
			elif gameAdded == 3: # 3 will be go fish
				player2Add.status = "Go Fish"
				#self.goFishGame.playerList.append(player2add) #added to go fish player list
			elif gameAdded == 4: # 4 will be roulette
				player2add.status = "Roulete"
				#self.rouletteGame.playerList.append(player2add) #added to the roulette player list
			else: #5 was selected, 5 will be horse betting
				player2add.status = "Horse Betting"
				#self.horseBetting.playerList.append(player2add) #added to the horse betting player list

                        self.customers.append(player2add) #adds as active player to casino
                        self.leaderboard.append(player2add) #adds player record to casino
		
		elif playerAction == 2:
			player2delete = random.randint(0,custCount-1) #list will already be filled, int will be 0 to the last customer
			for people in customers:
				if people.playerNumber == player2delete:
					gameAt = people.status #will need to remove player from their game as well
					self.customers.remove(people) #remove player from active list, does not delete record
					for everyone in self.leaderboard:
						if everyone.playerNumber == player2delete:
							everyone.status = "OOH" #out of house
			if gameAt == "Poker":
				for players in self.pokerGame.playerList:
					if players.playerNumber == player2delete:
						self.pokerGame.playerList.remove(players)
			elif gameAt == "Blackjack":
				for players in self.blackjackGame.playerList:
					if players.playerNumber == player2delete:
						self.blackjackGame.playerList.remove(players)
			elif gameAt == "Go Fish":
				for players in self.fishGame.playerList:
					if players.playerNumber == player2delete:
						self.fishGame.playerlist.remove(players)
			elif gameAt == "Roulette":
				for players in self.rouletteGame.playerList:
					if players.playerNumber == player2delete:
						self.rouletteGame.playerList.remove(players)
			elif gameAt == "Horse Betting":
				for players in self.horseBetting.playerList:
					if players.playerNumber == player2delete:
						self.horseBetting.playerList.remove(players)

		elif playerAction == 3:
			playerMoving = player(1000)
			player2move = random.randint(0,custCount-1)
			gameTo = random.randint(1,4) #player will have 4 possible games to join from the one they are leaving
			for people in self.customers:
				if people.playerNumber == player2move:
					gameAt = people.status
					if gameAt == "Poker":
						for players in self.pokerGame.playerList:
							if players.playerNumber == player2move:
								playerMoving = players
								self.pokerGame.playerList.remove(players)
								if gameTo == 1: #poker to blackjack
									playerMoving.status = "Blackjack" #will this change the values in customer/leaderboard
									self.blackjackGame.playerList.append(playerMoving)
								elif gameTo == 2: #poker to Go fish
									playerMoving.status = "Go Fish" 
									self.fishGame.playerList.append(playerMoving)
								elif gameTo == 3: #poker to roulette
									playerMoving.status = "Roulette"
									self.rouletteGame.playerList.append(playerMoving)
								else: #poker to horse betting
									playerMoving.status = "Horse Betting"
									self.horseBetting.playerList.append(playerMoving)
					elif gameAt == "Blackjack":
						for players in self.blackjackGame.playerList:
							if players.playerNumber == player2move:
								playerMoving = players
								self.blackjackGame.playerList.remove(players)
								if gameTo == 1: #blackjack to poker
									playerMoving.status = "Poker"
									self.pokerGame.playerList.append(playerMoving)
								elif gameTo == 2: #blackjack to Go Fish
									playerMoving.status = "Go Fish"
									self.fishGame.playerList.append(playerMoving)
								elif gameTo == 3: #blackjack to roulette
									playerMoving.status = "Roulette"
									self.rouletteGame.playerList.append(playerMoving)
								else: #blackjack to horse betting
									playerMoving.status = "Horse Betting"
									self.horseBetting.playerList.append(playerMoving)
					elif gameAt == "Go Fish":
						for players in self.fishGame.playerList:
							if players.playerNumber == player2move:
								playerMoving = players
								self.fishGame.playerList.remove(players)
								if gameTo == 1: #go fish to poker
									playerMoving.status == "Poker"
									self.pokerGame.playerList.append(playerMoving)
								elif gameTo == 2: #go fish to blackjack
									playerMoving.status = "Blackjack"
									self.blackjackGame.playerList.append(playerMoving)
								elif gameTo == 3: #go fish to Roulette
									playerMoving.status = "Roulette"
									self.rouletteGame.playerList.append(playerMoving)
								else: #go fish to Horse Betting
									playerMoving.status = "Horse Betting"
									self.horseBetting.playerList.append(playerMoving)
                                        elif gameAt == "Roulette":
                                                for players in self.rouletteGame.playerList:
                                                        if players.playerNumber == player2move:
                                                                playerMoving = players
                                                                self.rouletteGame.playerList.remove(players)
                                                                if gameTo == 1: #roulette to poker
                                                                        playerMoving.status == "Poker"
                                                                        self.pokerGame.playerList.append(playerMoving)
                                                                elif gameTo == 2: #roulette to blackjack
                                                                        playerMoving.status = "Blackjack"
                                                                        self.blackjackGame.playerList.append(playerMoving)
                                                                elif gameTo == 3: #roulette to go fish
                                                                        playerMoving.status = "Go Fish"
                                                                        self.fishGame.playerList.append(playerMoving)
                                                                else: #go fish to Horse Betting
                                                                        playerMoving.status = "Horse Betting"
                                                                        self.horseBetting.playerList.append(playerMoving)
                                        elif gameAt == "Horse Betting":
                                                for players in self.horseBetting.playerList:
                                                        if players.playerNumber == player2move:
                                                                playerMoving = players
                                                                self.horseBetting.playerList.remove(players)
                                                                if gameTo == 1: #horse betting to poker
                                                                        playerMoving.status == "Poker"
                                                                        self.pokerGame.playerList.append(playerMoving)
                                                                elif gameTo == 2: #horse betting to blackjack
                                                                        playerMoving.status = "Blackjack"
                                                                        self.blackjackGame.playerList.append(playerMoving)
                                                                elif gameTo == 3: #horse betting to Roulette
                                                                        playerMoving.status = "Roulette"
                                                                        self.rouletteGame.playerList.append(playerMoving)
                                                                else: #horse betting to go fish
                                                                        playerMoving.status = "Go Fish"
                                                                        self.fishGame.playerList.append(playerMoving)
					for people in customers:
						if people.playerNumber == player2move:
							people.status == playerMoving.status
					for people in leaderboard:
						if people.playerNumber == player2moce:
							people.status == playerMoving.status	
		

	def updateBoards(self):
		for people in self.pokerGame.playerList:
			people.plusMinus = people.balance - people.startingBalance
			for custs in self.customers:
				if people.playerNumber == custs.playerNumber:
					custs.balance = people.balance
					custs.plusMinus = people.plusMinus
			for leaders in self.leaderboard:
				if people.playerNumber == leaders.playerNumber:
					leaders.balance = people.balance
					leaders.plusMinus = people.plusMinus
		for people in self.blackjackGame.playerList:
			people.plusMinus = people.balance - people.statingBalance
			for custs in self.customers:
                                if people.playerNumber == custs.playerNumber:
                                        custs.balance = people.balance
                                        custs.plusMinus = people.plusMinus
                        for leaders in self.leaderboard:
                                if people.playerNumber == leaders.playerNumber:
                                        leaders.balance = people.balance
                                        leaders.plusMinus = people.plusMinus
                for people in self.fishGame.playerList:
                        people.plusMinus = people.balance - people.statingBalance
                        for custs in self.customers:
                                if people.playerNumber == custs.playerNumber:
                                        custs.balance = people.balance
                                        custs.plusMinus = people.plusMinus
                        for leaders in self.leaderboard:
                                if people.playerNumber == leaders.playerNumber:
                                        leaders.balance = people.balance
                                        leaders.plusMinus = people.plusMinus
                for people in self.rouletteGame.playerList:
                        people.plusMinus = people.balance - people.statingBalance
                        for custs in self.customers:
                                if people.playerNumber == custs.playerNumber:
                                        custs.balance = people.balance
                                        custs.plusMinus = people.plusMinus
                        for leaders in self.leaderboard:
                                if people.playerNumber == leaders.playerNumber:
                                        leaders.balance = people.balance
                                        leaders.plusMinus = people.plusMinus
                for people in self.horseBetting.playerList:
                        people.plusMinus = people.balance - people.statingBalance
                        for custs in self.customers:
                                if people.playerNumber == custs.playerNumber:
                                        custs.balance = people.balance
                                        custs.plusMinus = people.plusMinus
                        for leaders in self.leaderboard:
                                if people.playerNumber == leaders.playerNumber:
                                        leaders.balance = people.balance
                                        leaders.plusMinus = people.plusMinus


	def runCasino(self):
		for i in range(self.rounds):
			if self.poker == 1:
				self.pokerGame.playRound()
			if self.blackjack == 1:
				self.blackjackGame.playRound()
			if self.fish == 1:
				self.goFishGame.playRound()
			if self.roulette == 1:
				self.rouletteGame.playRound()
			if self.horses == 1:
				self.horseBetting.playRound()
			self.updateBoards()
			self.playerControl()

	def printStats(self):
		self.profit = self.pokerGame.casinoWinnings + self.blackjackGame.casinoWinnings + self.fishGame.casinoWinnings + self.rouletteGame.casinoWinnings + self.horseBetting.casinoWinnings
		#poker
		print "Poker Stats:"
		print "     Casino Winnings from Poker: $", self.pokerGame.casinoWinnings
		pokerPercent = (self.pokerGame.casinoWinnings/self.profit) * 100 #percent profit from poker
		print "       Percent:", pokerPercent, "%"
		averageAnte = (self.pokerGame.casinoWinnings /self.pokerGame.rake) / self.rounds #casino winnings = ante * rake => ante = casino winnings/rake, divide by rounds to find average
		print "     Average Ante: $", averageAnte, 
		print "     Rake Percent:", (self.pokerGame.rake * 100),"%"
		#blackjack
		print "Blackjack Stats:"
		print "     Casino Winnings from Blackjack: $", self.blackjackGame.casinoWinnings
		bjPercent = (self.blackjackGame.casinoWinnings/self.profit) * 100 #percent profit from blackjack
		print "       Percent:", bjPercent, "%"
		#calculate average bet?
		print "     Dealer Hard Stand:", self.blackjackGame.dealerStand 
		#calculate times dealer busts based on hard stand value?
		#Go Fish
		print "Go Fish Stats:"
		print "     Casino winnings from Go Fish: $", self.fishGame.casinoWinnings
		fishPercent = (self.fishGame.casinoWinnings/self.profit) * 100 #percent profit from Go Fish
		print "       Percent:", fishPercent, "%"
		print "     Table Minimum: $", self.fishGame.tableMin
		print "     Table Vig:", self.fishGame.vig, "%"
			## Other Fish Stats?
		#roulette
		print "Roulette Stats:"
		print "     Casino Winnings from Roulette: $", self.rouletteGame.casinoWinnings
		roulettePercent = (self.rouletteGame.casinoWinnings/self.profit) * 100 #percent profit from Roulette
		print "       Percent:", roulettePercent, "%"
		print "     Table Minimum: $", self.rouletteGame.tableMin
			## player win rate?
		#horse betting
		print "Horse Betting Stats:"
		print "     Casino Winnings from Horse Betting: $", self.horseBetting.casinoWinnings
		horsePercent = (self.horseBetting.casinoWinnings/self.profit) * 100 #percent profit from horse betting
		print "       Percent:", horsePercent, "%"
		print "     Accuracy of Odds:", self.horseBetting.accuracyRate, "%"
			## player win rate from odds

	def printPlayer(self, index):
                print "Player Number:", self.leaderboard[index].playerNumber
                print "Overall Winnings:", self.leaderboard[index].plusMinus
                print "Player Type:", self.leaderboard[index].playType
		print "Player Status:", self.leaderboard[index].status

	def printLeaderboard(self):
		for people in self.leaderboard:
			people.plusMinus = people.balance - people.startingBalance #sets all players final over/under of starting balance
		self.leaderboard.sort(key = lambda x: x.plusMinus) #will sort leaderboard based on the final over/under of starting balance
		for i in range(len(self.leaderboard)):
			if i == 0: #top player of the "night" (1 full simulation)
				print "======= Top Whales ======="
				print "The top whale of the night was:"
				printPlayer(i)
			elif i == 1: #second player
				print "The second place player of the night was:"
				printPlayer(i)
			elif i == 2: #third player
				print "The third place player of the night was:"
				printPlayer(i)
				print "=========================="
			elif i == len(self.leaderboard) - 3: #third worst player
				print "====== Bottom Fish ======"
				print "The third worst player of the night was:"
				printPlayer(i)
			elif i == len(self.leaderboard) - 2:
				print "The second worst player of the night was:"
                                printPlayer(i)
			elif i == len(self.leaderboard) -1 : #worst player
				print "The fish of the night was:"
                                printPlayer(i)
				print "========================="
			else: #any player in the middle
				printPlayer(i)
			
	def play(self):
		print "Welcome to the Casino Simulator"
		while quit != 0:
			self.playerInstantiation()
			self.simMenu()
			self.runCasino()
			self.printStats()
			self.printLeaderboard()
			choice = input("Would you like to run another simulation? Yes[1]/No[0]: ")
			if choice != 1:
				quit = 1
				print "Thank you for playing."			

class player():
	startingBalance = 0
	balance = 0 #current balance
	plusMinus = 0 
	playType = 0
	status = " "
	bluff = 0
   	BigBlind = 0
    	SmallBlind = 0
    	bet = 0.0
    	bet2 = 0.0
    	allIn = 0
    	fold = 0
    	playerNumber = 0
    	def __init__(self, num):
		self.playerNumber = num
        	self.balance = random.randint(40000, 55000)
		self.startingBalance = self.balance
        	self.playType = random.randint(1,3)
		self.localHand = hand(num)
		#print "Player", self.playerNumber
		#print self.balance
		#print self.playType
    	def subMoney(self, money):
		self.balance = self.balance - money
    	def addMoney(self, money):
        	self.balance = self.balance + money
    	def placeBet(self):
		betPer = 0.0
        	if self.playType == 3:
        		bluff = random.randint(1,20) #gives player type 3 a 5% chance of bluffing
            	if bluff == 20:
                	self.bluff = 1
                	betPer = random.randint(15,25) #bluff bets 15 to 25 percent on first bet
                	self.bet = betPer * self.balance / 100
                	return self.bet
        	if self.localHand.handValue == 1: #player has high card
            		if self.playType == 1:
                		self.fold = 1
                		self.bet = 0
                		return 0 #returning a 0 will be a fold, player type 1 folds on high card for safety
            		else:
                		betPer = random.randint(4,6) #player type 2 and 3 bet 4 to 6 percent on hgih card hands
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 2: #player has pair
            		if self.playType == 1:
                		betPer = random.randint(4,6) #player type 1 will bet 4 to 6%
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(3,7) #player type 2 and 3 will bet 3 to 7 percent on a pair
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 3: #player has 2 pair
            		if self.playType == 1:
                		betPer = random.randint(4,6) #player type 1 betse 4 to 6 percent on 2 pair
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(6,10) #player type 2 and 3 bet 6 to 10 percent on 2 pair
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 4: #player has 3 of a kind
            		if self.playType == 1:
                		betPer = random.randint(7,9) #plaer type 1 only bets 7 to 9 percent on 3 of a kind
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(7, 13) #player type 2 and 3 will bet 7 to 13 percent on 3 of a kind
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 5: #player has a Straight
            		if self.playType == 1:
                		betPer = random.randint(7,9) #player type 1 will bet 7 to 9 percent on a straight
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(7,13) #player type 2 and 3 will bet 7 to 13 percent on a straight
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 6: #player has flush
            		if self.playType == 1:
                		betPer = random.randint(8,12) #player type 1 will bet 8 to 12 percent on a flush
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(10,20) #player type 2 and 3 will bet 10 to 20 percent on a flush
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 7: #player has full house
            		if self.playType == 1:
                		betPer = random.randint(13,17) #player type 1 will bet 13 to 17 % on a full house
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(10,20) #player type 2 nd 3 will bet 10 to 20 percent on a full house
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 8: #player has 4 of a kind
            		if self.playType == 1:
                		betPer = random.randint(18,22) #player type 1 bets 18 to 22 percent on 4 of a kind
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(10,20) #player 2 and 3 bet 10 to 20 percent on 4 of a kind
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	elif self.localHand.handValue == 9: #player has a straight flush
            		if self.playType == 1:
                		betPer = random.randint(18,22) #player 1 bets 18 to 22 percent on a straight flush
                		self.bet = betPer * self.balance / 100
                		return self.bet
            		else:
                		betPer = random.randint(15,25) #player type 2 and 3 bets 15 to 25 percent on straight flush
                		self.bet = betPer * self.balance / 100
                		return self.bet
        	else: #player has royal flush
            		if self.playType == 1:
                		self.bet = self.balance #player type 1 goes all in on royal flush
				self.allIn = 1
                		return self.bet
            		else:
                		betPer = random.randint(15,25) #player type 2 and 3 bets 15 to 25 percent on royal flush
                		self.bet = betPer * self.balance / 100
                		return self.bet
	def placeBet2(self):
        	if self.bluff == 1:
            		betPer = random.randint(25,35) #bluff bets 25 to 35 percent on bet
            		self.bet2 = betPer * self.balance / 100
            		return self.bet2
        	if self.allIn == 1:
            		self.bet2 = 0
            		return 0
		if self.fold == 1:
	    		self.bet2 = 0
	    		return 0
        	if self.localHand.handValue == 1: #player has high card
            		if self.playType == 1:
                		return 0 #returning a 0 will be a fold, player type 1 folds on high card for safety
            		else:
                		betPer = random.randint(4,6) #player type 2 and 3 bet 4 to 6 percent on hgih card hands
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 2: #player has pair
            		if self.playType == 1:
                		betPer = random.randint(4,6) #player type 1 will bet 4 to 6%
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(3,7) #player type 2 and 3 will bet 3 to 7 percent on a pair
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 3: #player has 2 pair
            		if self.playType == 1:
                		betPer = random.randint(4,6) #player type 1 betse 4 to 6 percent on 2 pair
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(6,10) #player type 2 and 3 bet 6 to 10 percent on 2 pair
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 4: #player has 3 of a kind
            		if self.playType == 1:
                		betPer = random.randint(7,9) #plaer type 1 only bets 7 to 9 percent on 3 of a kind
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(7, 13) #player type 2 and 3 will bet 7 to 13 percent on 3 of a kind
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 5: #player has a Straight
            		if self.playType == 1:
                		betPer = random.randint(7,9) #player type 1 will bet 7 to 9 percent on a straight
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(12,18) #player type 2 and 3 will bet 12 to 19 percent on a straight
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 6: #player has flush
            		if self.playType == 1:
                		betPer = random.randint(8,12) #player type 1 will bet 8 to 12 percent on a flush
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(15,25) #player type 2 and 3 will bet 15 to 25 percent on a flush
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 7: #player has full house
            		if self.playType == 1:
                		betPer = random.randint(13,17) #player type 1 will bet 13 to 17 % on a full house
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(15,25) #player type 2 nd 3 will bet 15 to 25 percent on a full house
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 8: #player has 4 of a kind
            		if self.playType == 1:
                		betPer = random.randint(18,22) #player type 1 bets 18 to 22 percent on 4 of a kind
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(20,30) #player 2 and 3 bet 20 to 30 percent on 4 of a kind
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	elif self.localHand.handValue == 9: #player has a straight flush
            		if self.playerType == 1:
                		betPer = random.randint(18,22) #player 1 bets 18 to 22 percent on a straight flush
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
            		else:
                		betPer = random.randint(20,30) #player type 2 and 3 bets 20 to 30 percent on straight flush
                		self.bet2 = betPer * self.balance / 100
                		return self.bet2
        	else: #player has royal flush
            		if self.playType == 1:
                		self.bet2 = self.balance #player type 1 goes all in on royal flush
                		self.allIn = 1
                		return self.bet2
            		else:
                		self.bet2 = self.balance
                		self.allIn = 1
                		return self.bet2

newCasino = casino()
newCasino.play()