import random
from array import *

class pokerGame:
    playerList = []
    numPlayers = len(playerList) # min 3, limit 8
    gamesPlayed = 0 #keeps track for simulation
    casinoProfit = 0 #rake will be 3% of ante
    ante = 0

    def __init__(self):  #constuctor for a game to always instantiate 3 people
        for i in range(3):
            newPlayer = player()
            playerList.append(newPlayer)

    def playRound(self):
	setBlind()
	determineHand()
	introBets()
	dealRound()
	determineHand()
	placeBets()
	switchCards()
	placeBets()

class player:
    balance = 0
    playType = 0
    BigBlind = 0
    SmallBlind = 0

    def __init__(self):
        balance = randStart.randint(40000, 55000)
        playType = randType.randint(1,4)

    def subMoney(self, money):
	balance = balance - money;

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
            cValues[cardNum] = random.randint(1, 14)
            sValues[cardNum] = rand.randint(1, 5)
        setCards()
        setSuits()
        for i in self.cards:
            print cards[i]

    def setCards(self):
        for x in self.cValues:
            if (cValues[x] > 1) or (cValues[x] < 11):
                cards[x] = str(values[x])
            elif cValues[x] == 1:
                cards[x] = "A"
            elif cValues[x] == 11:
                cards[x] = "J"
            elif cValues[x] == 12:
                cards[x] = "Q"
            else:
                cards[x] = "K"
    def setSuits():
        for x in self.sValues:
            if sValue[x] == 1:
                suits[x] = "H"
            elif sValues[x] == 2:
                suits[x] = "D"
            elif sValues[x] == 3:
                suits[x] = "C"
            else:
                suits[x] = "S"
