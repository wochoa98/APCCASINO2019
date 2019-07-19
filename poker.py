import random
from array import *

class poker:
    	gamesPlayed = 0 #keeps track for simulation
    	casinoProfit = 0
    	rake = 0.03 #rake will be 3% of ante
    	ante = 0

    	def __init__(self):  #constuctor for a game sets list to length 6 which is what the simulator will command it to do
        	self.playerList = [] #declare in constructor so that it may be manipulated by simulator

    	def setBlind(self):
		if self.gamesPlayed == 0: #if no one has played yet, big blind starts at player 0
            		self.playerList[0].BigBlind = 1
	    		self.playerList[1].SmallBlind = 0
            		self.gamesPlayed = 1
        	else:
	    		for players in playerList:
	        		if players.BigBlind == 1:
	            			players.BigBlind = 0
	            			players.SmallBlind = 1
	            			if players == playerList[-1]:
		        			self.playerList[0].BigBlind = 1
		    			else:
    	                			players += 1
	                			players.BigBlind = 1
                        			break

    	def determineHand(self):
	    	for i in range(3):
	        	self.playerList[i].localHand.setHighCard()
                	self.playerList[i].localHand.hasPair()
                	self.playerList[i].localHand.hasTwoPair()
                	self.playerList[i].localHand.hasThree()
                	self.playerList[i].localHand.hasFullHouse()
                	self.playerList[i].localHand.hasFour()
                	self.playerList[i].localHand.hasFlush()

    	def introBets(self): #for start of game with big/small blind
		for players in self.playerList:
	    		if players.BigBlind == 1:
	        		players.subMoney(0) #already ante'd up
	    		elif players.SmallBlind == 1:
	        		players.subMoney(500)
	        		self.ante = self.ante + 500
	    		else:
	        		players.subMoney(1000)
	        		self.ante = self.ante + 1000

    	def dealRound(self):
		for m in range(3):
	    		for n in range(5):
				if self.playerList[m].localHand.playerNum == self.playerList[m].playerNumber:
		    			self.playerList[m].localHand.cValues[n] = self.playerList[m].localHand.dealCard()
		    			self.playerList[m].localHand.sValues[n] = self.playerList[m].localHand.dealCardSuit()

    	def playRound1(self):
        	highBet = 0
        	playerWithHighBet = 0
        	playerNum = 0
        	for players in self.playerList:
            		playerNum += 1
            		bet1 = players.placeBet()
            		if (highBet > bet1 * 1.1) and (players.allIn != 1): #if bet is outside of 10% of intended bet, the players will fold unless they are all in
                		players.fold = 1
                		players.bet = 0
            		elif (highBet < bet1 * 1.1) and (highBet > bet1 * 0.9): #bet is within 10% tolerance of intended bet, so they call
                		players.bet = highBet
            		else: #highbet is less than 90% of intended bet, so the player raises
                		highBet = players.bet
                		playerWithHighBet = playerNum
        	counter = 0
        	for players in self.playerList: #now reiterate through for players who have not matched the high bet
            		counter += 1
            		if counter >= playerWithHighBet: #bet returns to player with the high bet
                		break #betting is over
            		if highBet > (player.bet * 1.1): #if the new bet is outside of their tolerance
                		players.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
            		elif highBet <= (bet1 * 1.1): #bet is within 10% tolerance of intended bet, so they call
                		players.bet = highBet #sets for call
        	for players in self.playerList:
            		players.subMoney(players.bet)
            		self.ante = self.ante + players.bet

    	def playRound2(self):
        	highBet = 0
        	playerWithHighBet = 0
        	playerNum = 0
        	for players in self.playerList:
            		playerNum += 1
            		bet2 = players.placeBet2()
            		if (highBet > bet2 * 1.1) and (players.allIn != 1): #if bet is outside of 10% of intended bet, the players will fold unless they are all in
                		players.fold = 1
                		players.bet2 = 0
            		elif (highBet < bet2 * 1.1) and (highBet > bet2 * 0.9): #bet is within 10% tolerance of intended bet, so they call
                		players.bet2 = highBet
            		else: #highbet is less than 90% of intended bet, so the player raises
                		highBet = players.bet2
                		playerWithHighBet = playerNum
        	counter = 0
        	for players in self.playerList: #now reiterate through for players who have not matched the high bet
            		counter += 1
            		if counter >= playerWithHighBet: #bet returns to player with the high bet
                		break #betting is over
            		if highBet > (players.bet2 * 1.1): #if the new bet is outside of their tolerance
                		players.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
            		elif highBet < (players.bet2 * 1.1): #bet is within 10% tolerance of intended bet, so they call
                		players.bet2 = highBet #sets for call
        	for players in self.playerList:
            		players.subMoney(players.bet2)
            		self.ante = self.ante + players.bet

    	def selectWinner(self):
        	highHand = 0
        	count = 0
		contenders = []
		for players in self.playerList:
	    		if players.fold != 1:
				contenders.append(players)
        	for players in contenders:
            		if players.localHand.handValue > highHand:
                		count = 1
                		highHand = players.localHand.handValue
            		elif players.localHand.handValue == highHand:
                		count += 1
        	if count == 1: #if there are no competing winnings hands
            		for players in contenders: #find player and add winnings
                		if players.localHand.handValue == highHand:
                    			winnings = self.ante * (1 - self.rake)
                    			casinoWinnings = self.ante * self.rake
                    			players.balance = players.balance + winnings
                    			self.casinoProfit = self.casinoProfit + casinoWinnings
        	else: #there are competing winning hands
            		highCardHolder = [] #holds high card
            		lowCardHolder = [] #holds second high card to break high card tie
	    		indexer = 0
            		for players in contenders: #find their high cards
                		if players.localHand.handValue == highHand:
                    			highCardHolder.append(players.localHand.highCard)
                    			lowCardHolder.append(players.localHand.highCard2)
                    			indexer += 1
            		winningCard = 0
            		winningCard2 = 0
            		counter = 0
            		for i in highCardHolder:
                		if i > winningCard:
                    			winningCard = i
            		for j in highCardHolder:
                		if j == winningCard:
                    			counter += 1
            		if counter == 1: #if there are no competing high cards
                		for players in contenders:
                    			if (players.localHand.handValue == highHand) and (players.localHand.highCard == winningCard):
                        			winnings = self.ante * (1 - self.rake)
                        			casinoWinnings = self.ante * self.rake
                        			players.balance = players.balance + winnings
                        			self.casinoProfit = self.casinoProfit + casinoWinnings
            		else: #if counter > 1, therefore there are matching high cards
                		for k in lowCardHolder:
                    			if k > winningCard2:
                        			winningCard2 == k
                		for l in lowCardHolder:
                    			if l == winningCard:
                        			counter += 1
                		if counter == 1: #if high cards compete but low cards do not
                    			for players in contenders:
                        			if (players.localHand.handValue == highHand) and (players.localHand.highCard == winningCard) and (players.localHand.highCard2 == winningCard2):
                            				winnings = self.ante * (1 - self.rake)
                            				casinoWinnings = self.ante * self.rake
                            				players.balance = players.balance + winnings
                            				self.casinoProfit = self.casinoProfit + casinoWinnings
                				else: #if high and low cards compete, aka same exact hands
                    					totalWinnings = self.ante * (1 - self.rake)
                    					winnings = totalWinnings/counter
                    					for players in contenders:
                        					if (players.localHand.handValue == highHand) and (players.localHand.highCard == winningCard) and (players.localHand.highCard2 == winningCard2):
                            						casinoWinnings = self.ante * self.rake
                            						self.casinoProfit = self.casinoProfit + casinoWinnings
                            						players.balance = players.balance + winnings

    	def resetPlayers(self):
        	for players in self.playerList:
            		players.allIn = 0
            		players.fold = 0
            		players.bet = 0
            		players.bet2 = 0
            		players.bluff = 0

#check this function with carpenter

    	def switchCards(self):
        	for players in self.playerList:
            		if players.localHand.handValue == 1: #high card
                		switchNum = random.randint(2,4) #determines random of 2 to 4 for cards to switch
                		for i in range(switchNum):
                    			players.localHand.cValues[switchNum] = players.localHand.dealCard()
		    			players.localHand.sValues[switchNum] = players.localHand.dealCardSuit()
            		elif players.localHand.handValue == 2: #pair
                		for j in range(5):
                    			if players.localHand.cValues[j] != players.localHand.highCard:
                        			players.localHand.cValues[j] = players.localHand.dealCard()
						players.localHand.cValues[j] = players.localHand.dealCardSuit()
            		elif players.localHand.handValue == 3: #2 pair
                		for k in range(5):
                    			if (players.localHand.cValues[k] != players.localHand.highCard) and (players.localHand.cValues[k] != players.localHand.highCard2):
                        			players.localHand.cValues[k] = players.localHand.dealCard()
						players.localHand.sValues[k] = players.localHand.dealCardSuit()
            		elif players.localHand.handValue == 4: #3 of a kind
                		for l in range(5):
                    			if players.localHand.cValues[l] != players.localHand.highCard:
                        			players.localHand.cValues[l] = players.localHand.dealCard()
						players.localHand.sValues[l] = players.localHand.dealCardSuit()
            		elif players.localHand.handValue == 8: #4 of a kind
                		for m in range(5):
                    			if players.localHand.cValues[m] != players.localHand.highCard:
                        			players.localHand.cValues[m] = players.localHand.dealCard()
						players.localHand.sValues[m] = players.localHand.dealCardSuit()

    	def playRound(self):
	    	self.setBlind()
	    	self.introBets()
	    	self.dealRound()
	    	self.determineHand()
	    	self.playRound1()
	    	self.switchCards()
            	self.determineHand()
	    	self.playRound2()
            	self.selectWinner()
            	self.resetPlayers()
