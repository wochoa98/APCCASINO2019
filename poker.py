import random
from array import *

class pokerGame:
    playerList = []
    numPlayers = len(playerList) # min 3, limit 8
    gamesPlayed = 0 #keeps track for simulation
    casinoProfit = 0
    rake = 0.03 #rake will be 3% of ante
    ante = 0

    def __init__(self):  #constuctor for a game to always instantiate 3 people
        newPlayer1 = player(1)
        self.playerList.append(newPlayer1)
	newPlayer2 = player(2)
	self.playerList.append(newPlayer2)
	newPlayer3 = player(3)
	self.playerList.append(newPlayer3)		    

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
		print "Player Num:",self.playerList[i].playerNumber
	        self.playerList[i].localHand.setHighCard()
                self.playerList[i].localHand.hasPair()
                self.playerList[i].localHand.hasTwoPair()
                self.playerList[i].localHand.hasThree()
                self.playerList[i].localHand.hasFullHouse()
                self.playerList[i].localHand.hasFour()
                self.playerList[i].localHand.hasFlush()
		print "Player ", i+1, "has a hand value of: ", self.playerList[i].localHand.handValue

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

#    def dealRound(self):   #function that plays game round by round
#        for i in range(3): # deal cards to each player
#	    print "Player", i+1," has hand:"
#            self.playerList[i].localHand.dealCards()

    def dealRound(self):
	for m in range(3):
	    for n in range(5):
		if self.playerList[m].localHand.playerNum == self.playerList[m].playerNumber:
		    self.playerList[m].localHand.cValues[n] = self.playerList[m].localHand.dealCard()
		    self.playerList[m].localHand.sValues[n] = self.playerList[m].localHand.dealCardSuit()
		    print "Card", n+1,":", self.playerList[m].localHand.cValues[n], "Suit:", self.playerList[m].localHand.sValues[n]

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
		print "Player", players.playerNumber, "Folds"
            elif (highBet < bet1 * 1.1) and (highBet > bet1 * 0.9): #bet is within 10% tolerance of intended bet, so they call
                players.bet = highBet
		print "Player", players.playerNumber, "Calls", players.bet
            else: #highbet is less than 90% of intended bet, so the player raises
                highBet = players.bet
		print "Player", players.playerNumber, "Raises to", players.bet
                playerWithHighBet = playerNum
        counter = 0
        for players in self.playerList: #now reiterate through for players who have not matched the high bet
            counter += 1
            if counter >= playerWithHighBet: #bet returns to player with the high bet
                break #betting is over
            if highBet > (player.bet * 1.1): #if the new bet is outside of their tolerance
                players.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
		print "Player", players.playerNumber, "Folds on the raise"
            elif highBet <= (bet1 * 1.1): #bet is within 10% tolerance of intended bet, so they call
                players.bet = highBet #sets for call
		print "Player", players.playerNumber, "Calls", players.bet
        for players in self.playerList:
            players.subMoney(players.bet)
            self.ante = self.ante + players.bet
	print "End Round 1 ============="

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
		print "Player", players.playerNumber, "Folds"
            elif (highBet < bet2 * 1.1) and (highBet > bet2 * 0.9): #bet is within 10% tolerance of intended bet, so they call
                players.bet2 = highBet
		print "Player", players.playerNumber, "Calls", players.bet2
            else: #highbet is less than 90% of intended bet, so the player raises
                highBet = players.bet2
                playerWithHighBet = playerNum
		print "Player", players.playerNumber, "Raises to", players.bet2
        counter = 0
        for players in self.playerList: #now reiterate through for players who have not matched the high bet
            counter += 1
            if counter >= playerWithHighBet: #bet returns to player with the high bet
                break #betting is over
            if highBet > (players.bet2 * 1.1): #if the new bet is outside of their tolerance
                players.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
		print "Player", players.playerNumber, "Folds"
            elif highBet < (players.bet2 * 1.1): #bet is within 10% tolerance of intended bet, so they call
                players.bet2 = highBet #sets for call
		print "Player", players.playerNumber, "Calls", players.bet2
        for players in self.playerList:
            players.subMoney(players.bet2)
            self.ante = self.ante + players.bet2
	print "End Round 2 ========="

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
		    print "Player", players.playerNumber, "Wins"
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
			print "Player", players.playerNumber, "Wins"
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
			    print "Player", players.playerNumber, "Wins"
                else: #if high and low cards compete, aka same exact hands
                    totalWinnings = self.ante * (1 - self.rake)
                    winnings = totalWinnings/counter
                    for players in contenders:
                        if (players.localHand.handValue == highHand) and (players.localHand.highCard == winningCard) and (players.localHand.highCard2 == winningCard2):
                            casinoWinnings = self.ante * self.rake
                            self.casinoProfit = self.casinoProfit + casinoWinnings
                            players.balance = players.balance + winnings
			    print "Player", players.playerNumber, "Splits the Pot"

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
	index = 0
	for players in self.playerList:
		index += 1
		print "Player ", index, "after swap"
		for cards in players.localHand.cValues:
			print cards

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

class hand:
#    cValues = []
#    for i in range(5):
#        cValues.append(i)
#    sValues = []
#    for j in range(5):
#        sValues.append(j)
    playerNum = 0
    handValue = 0
    highCard = 0
    highCard2 = 0
    royal = [10,11,12,13,14]

    def __init__(self, num):
	self.playerNum = num
	self.cValues = []
	for z in range(5):
	    self.cValues.append(z)
	self.sValues = []
	for x in range(5):
	    self.sValues.append(x)	

    def dealCards(self):
        for a in range(5):
            card = random.randint(2, 14)
            self.cValues[a] = card
            suit = random.randint(1, 4)
            self.sValues[a] = suit
            print "Card:", self.cValues[a], "Suit:", self.sValues[a]

    def dealCard(self):
         cValue = random.randint(2,14)
         return cValue

    def dealCardSuit(self):
        sValue = random.randint(1,4)
        return sValue

#following functions adapted from http://pythonfiddle.com/poker-game/

    def hasFlush(self):
        suit = self.sValues[0]
	count = 0
        for i in range(5):
            if suit == self.sValues[i]:# if not a flush
     	        count += 1
	if count == 5:
            self.cValues.sort()
            for z in range(5):
                if self.cValues[z] == self.royal[z]: # if royal flush
		    self.handValue = 10
		else: #else, its a flush but not royal
                    low = min(self.cValues)   #check for other flushes
                    if (low + 1 in self.cValues) and (low + 2 in self.cValues) and (low + 3 in self.cValues) and (low + 4 in self.cValues): # if straight flush
                        self.handValue = 9
                        self.highCard = (low + 4)
                    else: # regular flush
                        if self.handValue > 6:
                            self.handValue = self.handValue
                        else:
                            self.handValue = 6
#       print "Player has hand value", self.handValue, "after checking for flushes"

    def hasStraight(self):
            self.cValues.sort()
            low = min(self.cValues)
            if (low + 1 in self.cValues) and (low + 2 in self.cValues) and (low + 3 in self.cValues) and (low + 4 in self.cValues): # if straight
                    self.handValue = 5
                    self.highCard = (low + 4)
#           print "Player has hand value", self.handValue, "after checking straight"

    def hasFullHouse(self):
            self.cValues.sort()
            cardA = self.cValues.count(self.cValues[0])
            cardB = self.cValues.count(self.cValues[4])
            if (cardA == 2 and cardB == 3):
                self.handValue = 7
                self.highCard = self.cValues[4]
                self.highCard2 = self.cValues[0]
            elif (cardA == 3 and cardB == 2):
                self.handValue = 7
                self.highCard = self.cValues[0]
                self.highCard2 = self.cValues[4]
#           print "Player card count A:", cardA
#           print "Player card count B:", cardB
#           print "Player has hand value", self.handValue, "after checking full house"

    def hasFour(self):
            self.cValues.sort()
            cardA = self.cValues.count(self.cValues[0])
            cardB = self.cValues.count(self.cValues[4])
            if cardA == 4: # player has 4 of a kind
                self.handValue = 8
                self.highCard = self.cValues[0]
            elif cardB == 4: # player again has 4 of a kind
                self.handValue = 8
                self.highCard = self.cValues[4]
#           print "Player card count A:", cardA
#           print "Player card count B:", cardB
#           print "Player has hand value", self.handValue, "after checking 4 of a kind"

    def hasThree(self):
            self.cValues.sort()
            cardA = self.cValues.count(self.cValues[0])
            cardB = self.cValues.count(self.cValues[4])
            if cardA == 3: # player has 3 of a kind
                self.handValue = 4
                self.highCard = self.cValues[0]
            elif cardB == 3:
                self.handValue = 4
                self.highCard = self.cValues[4]
#           print "Player card count A:", cardA
#           print "Player card count B:", cardB
#           print "Player has hand value", self.handValue, "after checking three of a kind"

    def hasTwoPair(self):
            self.cValues.sort()
            cardA = self.cValues.count(self.cValues[0])
            cardB = self.cValues.count(self.cValues[2])
            cardC = self.cValues.count(self.cValues[4])
            if (cardA == 2 and cardB == 2):
                self.handValue = 3
                self.highCard = self.cValues[2]
                self.highCard2 = self.cValues[0]
            elif (cardA == 2 and cardC == 2):
                self.handValue = 3
                self.highCard = self.cValues[4]
                self.highCard2 = self.cValues[0]
            elif (cardB == 2 and cardC == 2):
                self.handValue = 3
                self.highCard = self.cValues[4]
                self.highCard2 = self.cValues[2]
#           print "Player's card count A:", cardA
#           print "Player's card count B:", cardB
#           print "Players card count C:", cardC
#           print "Player has hand value", self.handValue, "after checking 2 pair"

    def hasPair(self):
        self.cValues.sort()
#       print "Checkin for pair \n"
#       for i in range(5):
#           print "Card", i+1, "is", self.cValues[i]
        cardA = self.cValues.count(self.cValues[0])
        cardB = self.cValues.count(self.cValues[2])
        cardC = self.cValues.count(self.cValues[4])
        if cardA == 2:
                self.handValue = 2
                self.highCard = self.cValues[0]
        elif cardB == 2:
                self.handValue = 2
                self.highCard = self.cValues[2]
        elif cardC == 2:
                self.handValue = 2
                self.highCard = self.cValues[4]
#       print "Players card count A:", cardA
#       print "Player's card count B:", cardB
#       print "Player's card count C:", cardC
#       print "Player has hand value", self.handValue, "after checking pair"

    def setHighCard(self):
        if self.cValues[0] == 1:
            self.highCard = 1
            self.handValue = 1
        else:
            self.highCard = self.cValues[4]
            self.handValue = 1
#       print "Player has hand value", self.handValue, "after setting high card"
#       print "The high card is", self.highCard


class player(pokerGame):
    balance = 0
    playType = 0
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
        self.playType = random.randint(1,3)
	self.localHand = hand(num)
	print "Player", self.playerNumber
	print self.balance
	print self.playType

    def subMoney(self, money):
	self.balance = self.balance - money

    def addMoney(self, money):
        self.balance = self.balance + money

    def placeBet(self):
	betPer = 0.0
        if self.playType == 3:
            bluff = random.randint(1,20) #gives player type 3 a 5% chance of betting
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

newGame = pokerGame()
newGame.playRound()
