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
        for i in range(3):
            newPlayer = player()
            playerList.append(newPlayer)

    def setBlind(self):
	    if gamesPlayed == 0: #if no one has played yet, big blind starts at player 0
                playerList[0].BigBlind = 1
	        playerList[1].SmallBlind = 0
                gamesPlayed = 1
	    else:
	        for players in playerList:
		        if players.BigBlind == 1:
		            players.BigBlind = 0
		            players.SmallBlind = 1
		            if players == playerList[-1]:
			            playerList[0].BigBlind = 1
		            else:
			            players += 1
			            players.BigBlind = 1
       		                    break

    def determineHand(self):
	    for players in playerList:
	        players.setHighCard()
                players.hasPair()
                players.hasTwoPair()
                players.hasThree()
                players.hasFullHouse()
                players.hasFour()
                players.hasFlush()

    def introBets(self): #for start of game with big/small blind
	    for players in playerList:
	        if players.BigBlind == 1:
		        players.subMoney(0) #already ante'd up
	        elif players.SmallBlind == 1:
		        players.subMoney(500)
		        ante = ante + 500
	        else:
		        players.subMoney(1000)
		        ante = ante + 1000

    def dealRound(self):   #function that plays game round by round
        for players in playerList: # deal cards to each player
            players.dealCards()

    def playRound1(self):
        highBet = 0
        playerWithHighBet = 0
        playerNum = 0
        for players in playerList:
            playerNum += 1
            bet1 = players.placeBet()
            if (highBet > bet1 * 1.1) and (self.allIn != 1): #if bet is outside of 10% of intended bet, the players will fold unless they are all in
                self.fold = 1
                self.bet = 0
            elif (highBet < bet1 * 1.1) and (highBet > bet1 * 0.9): #bet is within 10% tolerance of intended bet, so they call
                self.bet = highBet
            else: #highbet is less than 90% of intended bet, so the player raises
                highBet = self.bet
                playerWithHighBet = playerNum
        counter = 0
        for players in playerList: #now reiterate through for players who have not matched the high bet
            counter += 1
            if counter >= playerWithHighBet: #bet returns to player with the high bet
                break #betting is over
            if highBet > (self.bet * 1.1): #if the new bet is outside of their tolerance
                self.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
            elif highBet < (bet1 * 1.1): #bet is within 10% tolerance of intended bet, so they call
                self.bet = highBet #sets for call
        for players in playerList:
            self.subMoney(self.bet)
            ante = ante + self.bet

def playRound2(self):
    highBet = 0
    playerWithHighBet = 0
    playerNum = 0
    for players in playerList:
        playerNum += 1
        bet2 = players.placeBet2()
        if (highBet > bet2 * 1.1) and (self.allIn != 1): #if bet is outside of 10% of intended bet, the players will fold unless they are all in
            self.fold = 1
            self.bet2 = 0
        elif (highBet < bet2 * 1.1) and (highBet > bet2 * 0.9): #bet is within 10% tolerance of intended bet, so they call
            self.bet2 = highBet
        else: #highbet is less than 90% of intended bet, so the player raises
            highBet = self.bet2
            playerWithHighBet = playerNum
    counter = 0
    for players in playerList: #now reiterate through for players who have not matched the high bet
        counter += 1
        if counter >= playerWithHighBet: #bet returns to player with the high bet
            break #betting is over
        if highBet > (self.bet2 * 1.1): #if the new bet is outside of their tolerance
            self.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
        elif highBet < (bet1 * 1.1): #bet is within 10% tolerance of intended bet, so they call
            self.bet2 = highBet #sets for call
    for players in playerList:
        self.subMoney(self.bet2)
        ante = ante + self.bet2

    def placeBet(self):
        if self.playType == 3:
            bluff = random.randint(1,11) #gives player type 3 a 10% chance of betting
            if bluff == 10:
                self.bluff = 1
                betPer = random.randint(15,26) #bluff bets 15 to 25 percent on first bet
                self.bet = betPer * self.balance
                return self.bet
        if self.handValue == 1: #player has high card
            if self.playType == 1:
                self.fold = 1
                self.bet = 0
                return 0 #returning a 0 will be a fold, player type 1 folds on high card for safety
            else:
                betPer = random.randint(4,7) #player type 2 and 3 bet 4 to 6 percent on hgih card hands
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 2: #player has pair
            if self.playType == 1:
                betPer = random.randint(4,7) #player type 1 will bet 4 to 6%
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(3,8) #player type 2 and 3 will bet 3 to 7 percent on a pair
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 3: #player has 2 pair
            if self.playType == 1:
                betPer = random.randint(4,7) #player type 1 betse 4 to 6 percent on 2 pair
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(6,11) #player type 2 and 3 bet 6 to 10 percent on 2 pair
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 4: #player has 3 of a kind
            if self.playType == 1:
                betPer = random.randint(7,10) #plaer type 1 only bets 7 to 9 percent on 3 of a kind
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(7, 14) #player type 2 and 3 will bet 7 to 13 percent on 3 of a kind
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 5: #player has a Straight
            if self.playType == 1:
                betPer = random.randint(7,10) #player type 1 will bet 7 to 9 percent on a straight
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(7,14) #player type 2 and 3 will bet 7 to 13 percent on a straight
                self.bet = betPer * self.balance
                return self.bet
        elif self.handvalue == 6: #player has flush
            if self.playerType == 1:
                betPer = random.randint(8,13) #player type 1 will bet 8 to 12 percent on a flush
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(10,21) #player type 2 and 3 will bet 10 to 20 percent on a flush
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 7: #player has full house
            if self.playType == 1:
                betPer = random.randint(13,18) #player type 1 will bet 13 to 17 % on a full house
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(10,21) #player type 2 nd 3 will bet 10 to 20 percent on a full house
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 8: #player has 4 of a kind
            if self.playType == 1:
                betPer = random.randint(18,23) #player type 1 bets 18 to 22 percent on 4 of a kind
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(10,21) #player 2 and 3 bet 10 to 20 percent on 4 of a kind
                self.bet = betPer * self.balance
                return self.bet
        elif self.handValue == 9: #player has a straight flush
            if self.playerType == 1:
                betPer = random.randint(18,23) #player 1 bets 18 to 22 percent on a straight flush
                self.bet = betPer * self.balance
                return self.bet
            else:
                betPer = random.randint(15,26) #player type 2 and 3 bets 15 to 25 percent on straight flush
                self.bet = betPer * self.balance
                return self.bet
        else: #player has royal flush
            if self.playType == 1:
                self.bet = self.balance #player type 1 goes all in on royal flush
                return self.bet
            else:
                betPer = random.randint(15,26) #player type 2 and 3 bets 15 to 25 percent on royal flush
                self.bet = betPer * self.balance
                return self.bet

    def placeBet2(self):
        if self.bluff == 1:
            betPer = random.randint(25,35) #bluff bets 25 to 35 percent on bet
            self.bet2 = betPer * self.balance
            return self.bet2
        if self.allIn == 1:
            self.bet2 = 0
            return 0
        if self.handValue == 1: #player has high card
            if self.playType == 1:
                return 0 #returning a 0 will be a fold, player type 1 folds on high card for safety
            else:
                betPer = random.randint(4,7) #player type 2 and 3 bet 4 to 6 percent on hgih card hands
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 2: #player has pair
            if self.playType == 1:
                betPer = random.randint(4,7) #player type 1 will bet 4 to 6%
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(3,8) #player type 2 and 3 will bet 3 to 7 percent on a pair
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 3: #player has 2 pair
            if self.playType == 1:
                betPer = random.randint(4,7) #player type 1 betse 4 to 6 percent on 2 pair
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(6,11) #player type 2 and 3 bet 6 to 10 percent on 2 pair
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 4: #player has 3 of a kind
            if self.playType == 1:
                betPer = random.randint(7,10) #plaer type 1 only bets 7 to 9 percent on 3 of a kind
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(7, 14) #player type 2 and 3 will bet 7 to 13 percent on 3 of a kind
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 5: #player has a Straight
            if self.playType == 1:
                betPer = random.randint(7,10) #player type 1 will bet 7 to 9 percent on a straight
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(12,19) #player type 2 and 3 will bet 12 to 19 percent on a straight
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handvalue == 6: #player has flush
            if self.playerType == 1:
                betPer = random.randint(8,13) #player type 1 will bet 8 to 12 percent on a flush
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(15,26) #player type 2 and 3 will bet 15 to 25 percent on a flush
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 7: #player has full house
            if self.playType == 1:
                betPer = random.randint(13,18) #player type 1 will bet 13 to 17 % on a full house
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(15,26) #player type 2 nd 3 will bet 15 to 25 percent on a full house
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 8: #player has 4 of a kind
            if self.playType == 1:
                betPer = random.randint(18,23) #player type 1 bets 18 to 22 percent on 4 of a kind
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(20,31) #player 2 and 3 bet 20 to 30 percent on 4 of a kind
                self.bet2 = betPer * self.balance
                return self.bet2
        elif self.handValue == 9: #player has a straight flush
            if self.playerType == 1:
                betPer = random.randint(18,23) #player 1 bets 18 to 22 percent on a straight flush
                self.bet2 = betPer * self.balance
                return self.bet2
            else:
                betPer = random.randint(20,31) #player type 2 and 3 bets 20 to 30 percent on straight flush
                self.bet2 = betPer * self.balance
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

    def selectWinner(self):
        highHand = 0
        count = 0
        for players in playerList:
            if self.handValue > highHand:
                count = 1
                highHand = self.handValue
            elif self.handValue == highHand:
                count += 1
        if count == 1: #if there are no competing winnings hands
            for players in playerList: #find player and add winnings
                if self.handValue == highHand:
                    winnings = ante * (1 - rake)
                    casinoWinnings = ante * rake
                    self.balance = self.balance + winnings
                    casinoProfit = casinoProfit + casinoWinnings
        else: #there are competing winning hands
            highCardHolder = [] #holds high card
            lowCardHolder = [] #holds second high card to break high card tie
            indexer = 0
            for players in playerList: #find their high cards
                if self.handValue == highHand:
                    highCardHolder[indexer] = self.highCard
                    lowCardHolder[indexer] = self.highCard2
                    indexer += 1
            winningCard = 0
            winningCard2 = 0
            counter = 0
            for i in highCardHolder:
                if i == 1: # 1 is an ace, the highest card
                    winningCard == 1
                elif (i > winningCard) and (winningCard != 1):
                    winningCard = i
            for j in highCardHolder:
                if j == winningCard:
                    counter += 1
            if counter == 1: #if there are no competing high cards
                for players in playerList:
                    if (self.handValue == highHand) and (self.highCard == winningCard):
                        winnings = ante * (1 - rake)
                        casinoWinnings = ante * rake
                        self.balance = self.balance + winnings
                        casinoProfit = casinoProfit + casinoWinnings
            else: #if counter > 1, therefore there are matching high cards
                for k in lowCardHolder:
                    if k > winningCard2:
                        winningCard2 == k
                for l in lowCardHolder:
                    if l == winningCard:
                        counter += 1
                if counter == 1: #if high cards compete but low cards do not
                    for players in playerList:
                        if (self.handValue == highHand) and (self.highCard == winningCard) and (self.highCard2 == winningCard2):
                            winnings = ante * (1 - rake)
                            casinoWinnings = ante * rake
                            self.balance = self.balance + winnings
                            casinoProfit = casinoProfit + casinoWinnings
                else: #if high and low cards compete, aka same exact hands
                    totalWinnings = ante * (1 - rake)
                    winnings = totalWinnings/counter
                    for players in playerList:
                        if (self.handValue == highHand) and (self.highCard == winningCard) and (self.highCard2 == winningCard2):
                            casinoWinnings = ante * rake
                            casinoProfit = casinoProfit + casinoWinnings
                            self.balance = self.balance + winnings


    def resetPlayers(self):
        for players in playerList:
            self.allIn = 0
            self.fold = 0
            self.bet = 0
            self.bet2 = 0
            self.bluff = 0

    def switchCards(self):
        for players in playerList:
            if self.handValue == 1: #high card
                switchNum = random.randint(2,5) #determines random of 2 to 4 for cards to switch
                for i in range(switchNum):
                    self.cValues[switchNum] = dealCard()
            elif self.handValue == 2: #pair
                for cards in self.cValues:
                    if cards != self.highCard:
                        cards = dealCard()
            elif self.handValue == 3: #2 pair
                for cards in self.cValues:
                    if (cards != self.highCard) or (cards != self.highCard2):
                        cards = dealCard()
            elif self.handValue == 4: #3 of a kind
                for cards in self.cValues:
                    if cards != self.highCard:
                        cards = dealCard()
            elif self.handValue == 8: #4 of a kind
                for cards in self.cValues:
                    if cards != self.highCard:
                        cards = dealCard()

                

    def playRound(self):
	    setBlind()
	    introBets()
	    dealRound()
	    determineHand()
	    playRound1()
	    switchCards()
            determineHand()
	    playRound2()
            selectWinner()
            resetPlayers()

class player(pokerGame):
    balance = 0
    playType = 0
    bluff = 0
    BigBlind = 0
    SmallBlind = 0
    bet = 0
    bet2 = 0
    allIn = 0
    fold = 0

    def __init__(self):
        self.balance = random.randint(40000, 55000)
        self.playType = random.randint(1,4)

    def subMoney(self, money):
	    self.balance = self.balance - money

    def addMoney(self, money):
        self.balance = self.balance + money

class hand(player):
    cards = [5]
    cValues = [5]
    suits = [5]
    sValues = [5]
    handValue = 0
    highCard = 0
    highCard2 = 0
    royal = [1,10,11,12,13]

    def dealCards(self):
        for cardNum in self.cValues:
            self.cValues[cardNum] = random.randint(1, 14)
            self.sValues[cardNum] = random.randint(1, 5)
        setCards()
        setSuits()
        for i in self.cards:
            print self.cards[i]

    def dealCard(self):
         cValue = random.randint(1,14)
         return cValue

    def setCards(self):
        for x in self.cValues:
            if (self.cValues[x] > 1) or (self.cValues[x] < 11):
                self.cards[x] = str(self.values[x])
            elif self.cValues[x] == 1:
                self.cards[x] = "A"
            elif self.cValues[x] == 11:
                self.cards[x] = "J"
            elif self.cValues[x] == 12:
                self.cards[x] = "Q"
            else:
                self.cards[x] = "K"
    def setSuits(self):
        for x in self.sValues:
            if self.sValue[x] == 1:
                self.suits[x] = "H"
            elif self.sValues[x] == 2:
                self.suits[x] = "D"
            elif self.sValues[x] == 3:
                self.suits[x] = "C"
            else:
                self.suits[x] = "S"

    def hasFlush(self):
        suit = self.sValues[0]
	for i in self.sValues:
	        if suit != i:# if not a flush
	                self.handValue = self.handValue
	        else:# if flush
	            self.cValues.sort()
		    if cmp(self.cValues, self.royal): # if royal flush
		        self.handValue = 10
	            else:
		            low = min(self.cValues)
		            if (low + 1 in self.cValues) and (low + 2 in self.cValues) and (low + 3 in self.cValues) and (low + 4 in self.cValues): # if straight flush
			            self.handValue = 9
			            self.highCard = (low + 4)
		            else: # regular flush
	                        if self.handValue > 6:
        	                    self.handValue = self.handValue
                	        else:
		                    self.handValue = 6

    def hasStraight(self):
	    self.cValues.sort()
	    low = min(self.cValues)
            if (low + 1 in self.cValues) and (low + 2 in self.cValues) and (low + 3 in self.cValues) and (low + 4 in self.cValues): # if straight flush
		    self.handValue = 5
		    self.highCard = (low + 4)

    def hasFullHouse(self):
	    self.cValues.sort()
	    cardA = self.cValues.count(self.cValues[0])
	    cardB = self.cValues.count(self.cValues[4])
	    if (cardA == 2 and cardB == 3):
	        self.handValue = 7
	        self.highCard = cValues[4]
	        self.highCard2 = cValues[0]
	    elif (CardA == 3 and cardB == 2):
	        self.handValue = 7
	        self.highCard = cValues[0]
	        self.highCard2 = cValues[4]

    def hasFour(self):
	    self.cValues.sort()
            cardA = self.cValues.count(self.cValues[0])
	    cardB = self.cValues.count(self.cValues[4])
	    if cardA == 4: # player has 4 of a kind
	        self.handValue = 8
	        self.highCard = cValues[0]
	    elif cardB == 4: # player again has 4 of a kind
	        self.handValue = 8
	        self.highCard = cValues[4]

    def hasThree(self):
	    self.cValues.sort()
	    cardA = self.cValues.count(self.cValues[0])
	    cardB = self.cValues.count(self.cValues[4])
	    if cardA == 3: # player has 3 of a kind
	        self.handValue = 4
	        self.highCard = cValues[0]
	    elif cardB == 3:
	        self.handValue = 4
	        self.highCard = cValues[4]

    def hasTwoPair(self):
	    self.cValues.sort()
	    cardA = self.cValues.count(self.cValues[0])
	    cardB = self.cValues.count(self.cValues[2])
	    cardC = self.cValues.count(self.cValues[4])
	    if (cardA == 2 and cardB == 2):
	        self.handValue = 3
	        self.highCard = cValues[2]
	        self.highCard2 = cValues[0]
	    elif (cardA == 2 and cardC == 2):
	        self.handValue = 3
	        self.highCard = cValues[4]
	        self.highCard2 = cValues[0]
	    elif (cardB == 2 and cardC == 2):
	        self.handValue = 3
	        self.highCard = cValues[4]
	        self.highCard2 = cValues[2]

    def hasPair(self):
	self.cValues.sort()
        cardA = self.cValues.count(self.cValues[0])
        cardB = self.cValues.count(self.cValues[4])
        cardC = self.cValues.count(self.cValues[2])
	if cardA == 2:
	        self.handValue = 2
	        self.highCard = cValues[0]
	elif cardB == 2:
	        self.handValue = 2
	        self.highCard = cValues[2]
	elif cardC == 2:
	        self.handValue = 2
	        self.highCard = cValues[4]

    def setHighCard(self):
        self.cValues.sort()
        if self.cValues[0] == 1:
            self.highCard = 1
            self.handValue = 1
        else:
            self.highCard = self.cValues[4]
            self.handValue = 1



newGame = pokerGame()
playRound()

