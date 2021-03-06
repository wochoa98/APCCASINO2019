import random
from array import *

class poker:
    gamesPlayed = 0 #keeps track for simulation
    casinoWinnings = 0
    rake = 0.03 #rake will be 3% of ante

    def __init__(self):  #constuctor for a game sets list to length 6 which is what the simulator will command it to do
        self.playerList = [] #declare in constructor so that it may be manipulated by simulator
        self.ante = 0

    def setBuyIn(self):
        for players in self.playerList:
            players.subMoney(1000)
            self.ante = self.ante + 1000

    def determineHand(self):
        for i in range(len(self.playerList)):
            self.playerList[i].localHand.setHighCard()
            self.playerList[i].localHand.hasPair()
            self.playerList[i].localHand.hasTwoPair()
            self.playerList[i].localHand.hasThree()
            self.playerList[i].localHand.hasFullHouse()
            self.playerList[i].localHand.hasFour()
            self.playerList[i].localHand.hasFlush()
            
    def dealRound(self):
        for m in range(len(self.playerList)):
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
            #print ("Player", players.playerNumber, "intended to bet", bet1)
            if (highBet > bet1 * 1.1) and (players.allIn != 1): #if bet is outside of 10% of intended bet, the players will fold unless they are all in
                players.fold = 1
                players.bet = 0
            elif (highBet < bet1 * 1.1) and (highBet > bet1 * 0.9): #bet is within 10% tolerance of intended bet, so they call
                if highBet > players.balance:
                    players.bet = 0
                    players.fold = 1
                else:
                    players.bet = highBet #sets for call
            else: #highbet is less than 90% of intended bet, so the player raises
                highBet = players.bet
                playerWithHighBet = playerNum
        counter = 0
        for players in self.playerList: #now reiterate through for players who have not matched the high bet
            counter += 1
            if counter >= playerWithHighBet: #bet returns to player with the high bet
                break #betting is over
            if highBet > (players.bet * 1.1): #if the new bet is outside of their tolerance
                players.fold = 1 #they fold but they do not reset their bet, it will still be subtracted from their total
            elif highBet <= (bet1 * 1.1): #bet is within 10% tolerance of intended bet, so they call
                if highBet > players.balance:
                    players.bet = 0
                    players.fold = 1
                else:
                    players.bet = highBet #sets for call
        for players in self.playerList:
            players.balance = players.balance - players.bet
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
                if highBet > players.balance:
                    players.bet2 = 0
                    players.fold = 1
                else:
                    players.bet2 = highBet #sets for call
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
                if highBet > players.balance:
                    players.bet2 = 0
                    players.fold = 1
                else:
                    players.bet2 = highBet #sets for call

        for players in self.playerList:
            players.balance = players.balance - players.bet2
            self.ante = self.ante + players.bet2

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
                    casinoProfit = self.ante * self.rake
                    players.balance = players.balance + winnings
                    self.casinoWinnings = self.casinoWinnings + casinoProfit
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
                        casinoProfit = self.ante * self.rake
                        players.balance = players.balance + winnings
                        self.casinoWinnings = self.casinoWinnings + casinoProfit
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
                            casinoProfit = self.ante * self.rake
                            players.balance = players.balance + winnings
                            self.casinoWinnings = self.casinoWinnings + casinoProfit
                        else: #if high and low cards compete, aka same exact hands
                            totalWinnings = self.ante * (1 - self.rake)
                            winnings = totalWinnings/counter
                            for players in contenders:
                                if (players.localHand.handValue == highHand) and (players.localHand.highCard == winningCard) and (players.localHand.highCard2 == winningCard2):
                                    casinoProfit = self.ante * self.rake
                                    self.casinoWinnings = self.casinoWinnings + casinoProfit
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
        self.setBuyIn()
        self.dealRound()
        self.determineHand()
        self.playRound1()
        self.switchCards()
        self.determineHand()
        self.playRound2()
        self.selectWinner()
        self.resetPlayers()
        self.ante = 0
