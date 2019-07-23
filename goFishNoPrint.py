from array import *
import copy
import random

#Go-Fish

class goFish:

    def __init__(self):
        self.playerList = []
        self.inGameDeck = gameDeck()
        self.pot = 0
        self.winnings = 0
        self.casinoP = 0.1

    def playGame(self):

        print(len(self.playerList))

        self.buyIn()
        self.inGameDeck.dealHands(self.playerList)
        for p in self.playerList:
            print(p.playerHand)
        pn = 1
        round = 1

        self.inGameDeck.sortCards(self.playerList)
        while self.inGameDeck.gameEnd < len(self.playerList):
            for p in self.playerList:

                #Player Turn

                self.inGameDeck.sortCards(self.playerList)

                if(len(p.playerHand) != 0):
                    randPlayer = random.randint(1, len(self.playerList))

                    while((self.playerList[randPlayer-1].playerNumber == p.playerNumber)&(len(self.playerList[randPlayer-1].playerHand) > 0)):
                        randPlayer = random.randint(1, len(self.playerList))

                    askedCard = p.askRand()
                    self.playerList[randPlayer-1].askedPlayer(p, askedCard, self.inGameDeck)


                    self.inGameDeck.sortCards(self.playerList)
                    p.checkMatch()
                    self.inGameDeck.checkGameEnd(self.playerList)


                self.inGameDeck.refill(self.playerList)





                if(p.playerNumber == self.playerList[len(self.playerList)-1].playerNumber):
                    pn = 1

                else:
                    pn = pn + 1

            round = round + 1



        pn = 1
        for p in self.playerList:

            pn = pn+1

        self.whoWon()
        self.resetGame()

        #for p in self.playerList:







    def buyIn(self):
        temp = self.playerList
        for check in self.playerList:
            if(check.balance < 1000):

                self.playerList = [elem for elem in self.playerList if elem.playerNumber != check.playerNumber]

            else:
                self.pot = self.pot + 1000
                check.balance = check.balance - 1000


        if(self.pot > 0):
            casinoTake = self.pot*self.casinoP
            self.pot = self.pot - casinoTake
            self.winnings = self.winnings + casinoTake


    def whoWon(self):
        temp = [pop for pop in self.playerList]
        for p in self.playerList:
            for ps in self.playerList:
                if(p.matches > ps.matches):
                    temp = [pop for pop in temp if pop != ps]

        if(len(temp) > 0):
            payout = self.pot/len(temp)

            for paidPlayers in temp:

                paidPlayers.payDay(payout)



    def resetGame(self):
        self.inGameDeck.resetDeck()
        self.pot = 0
        self.inGameDeck.gameEnd = 0
        for p in self.playerList:
            p.playerHand = []
            p.matches = 0





class gameDeck:
    #cardValue = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13])
    #cardSuit = array('i', [1,2,3,4]) #1 = hearts, 2 = clubs, 3 = diamonds, 4 = spades


    def __init__(self):
        self.deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]  #0-12 = A-K Hearts || 13-25 = A-K Clubs || 26-38 = A-K Diamonds || 39-51 = A-K Spades
        self.cardsLeft = len(self.deck)
        self.gameEnd = 0

    def dealHands(self, players):
        c = 0
        for p in players:
            for c in range(4):
                cardNum = random.randint(0, len(self.deck)-1)
                p.addCard(self.deck[cardNum])
                self.deck.pop(cardNum)


    def resetDeck(self):
        self.deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]

    def refill(self, players):
        if(len(self.deck) > 0):
            for p in players:
                if(len(p.playerHand) <= 3):
                    temp = 4 - len(p.playerHand)
                    for i in range(temp):
                        if(len(self.deck) > 0):
                            cardNum = random.randint(0, len(self.deck)-1)
                            p.addCard(self.deck[cardNum])
                            self.deck.pop(cardNum)
                        else:
                            return


    def sortCards(self, players):
        for p in players:
            if(len(p.playerHand) > 0):
                p.playerHand.sort()



    def checkGameEnd(self, players):
        if(len(self.deck) == 0):
            count = 0
            for p in players:
                if(len(p.playerHand) == 0):
                    count = count + 1
            self.gameEnd = count


class goFishPlayer:

    def __init__(self, pn):
        self.playerHand = []
        self.matches = 0
        self.balance = 0
        self.playType = 0
        self.playerNumber = pn
        self.balance = 5000


    def checkMatch(self):
        if(len(self.playerHand) >= 4):
            cardCount = 0
            for i in range(len(self.playerHand)):

                if((self.playerHand[i] >= 0) & (self.playerHand[i] <= 12)):
                    cardCount = cardCount + 1


                    for a in range(len(self.playerHand)):
                        if(self.playerHand[a] == self.playerHand[i] + 13):
                            cardCount = cardCount + 1


                            for b in range(len(self.playerHand)):
                                if(self.playerHand[b] == self.playerHand[i] + 26):
                                    cardCount = cardCount + 1


                                    for c in range(len(self.playerHand)):
                                        if(self.playerHand[c] == self.playerHand[i] + 39):


                                            self.playerHand = [elem for elem in self.playerHand if elem != (self.playerHand[i] + 13)]
                                            self.playerHand = [elem for elem in self.playerHand if elem != (self.playerHand[i] + 26)]
                                            self.playerHand = [elem for elem in self.playerHand if elem != (self.playerHand[i] + 39)]
                                            self.playerHand = [elem for elem in self.playerHand if elem != (self.playerHand[i])]

                                            print(self.playerHand)
                                            self.matches += 1
                                            return
                                    return
                            return
                    return
            return

    def askRand(self):
        if(len(self.playerHand) > 0):
            randCard = random.randint(0, len(self.playerHand)-1)
            print(self.playerHand[randCard])
            returnVal = self.playerHand[randCard]
            return returnVal


    def askedPlayer(self, p, c, d):
        h = 0
        if(len(self.playerHand) > 0):
            for h in range(len(self.playerHand)):
                if(c <= 12):
                    if((self.playerHand[h] == c + 13)|(self.playerHand[h] == c + 26)|(self.playerHand[h] == c + 39)):
                        temp = [elem if elem == (c+13) else elem if elem == (c+26) else elem if elem == (c+39) else 100 for elem in self.playerHand]
                        temp = [elem for elem in temp if elem != 100]
                        self.playerHand = [elem for elem in self.playerHand if elem not in temp]
                        p.playerHand.extend(temp)

                        return

                    elif(h == len(self.playerHand)-1):
                        p.goFish(d)


                elif((c >= 13) & (c <= 25)):
                    if((self.playerHand[h] == c - 13)|(self.playerHand[h] == c + 13)|(self.playerHand[h] == c + 26)):
                        temp = [elem if elem == (c-13) else elem if elem == (c+13) else elem if elem == (c+26) else 100 for elem in self.playerHand]
                        temp = [elem for elem in temp if elem != 100]
                        self.playerHand = [elem for elem in self.playerHand if elem not in temp]
                        p.playerHand.extend(temp)

                        return

                    elif(h == len(self.playerHand)-1):
                        p.goFish(d)

                elif((c >= 26) & (c <= 38)):
                    if((self.playerHand[h] == c - 26)|(self.playerHand[h] == c - 13)|(self.playerHand[h] == c + 13)):
                        temp = [elem if elem == (c-26) else elem if elem == (c-13) else elem if elem == (c+13) else 100 for elem in self.playerHand]
                        temp = [elem for elem in temp if elem != 100]
                        self.playerHand = [elem for elem in self.playerHand if elem not in temp]
                        p.playerHand.extend(temp)

                        return

                    elif(h == len(self.playerHand)-1):
                        p.goFish(d)

                elif(c >= 39):
                    if((self.playerHand[h] == c - 39)|(self.playerHand[h] == c - 26)|(self.playerHand[h] == c - 13)):
                        temp = [elem if elem == (c-39) else elem if elem == (c-26) else elem if elem == (c-13) else 100 for elem in self.playerHand]
                        temp = [elem for elem in temp if elem != 100]
                        self.playerHand = [elem for elem in self.playerHand if elem not in temp]
                        p.playerHand.extend(temp)

                        return

                    elif(h == len(self.playerHand)-1):
                        p.goFish(d)


    def addCard(self, card):
        self.playerHand.append(card)

    def goFish(self, d):
        if(len(d.deck) > 0):
            cardNum = random.randint(0, len(d.deck)-1)
            self.addCard(d.deck[cardNum])
            d.deck.pop(cardNum)

    def resetHand(self):
        self.playerHand = []
        self.matches = 0

    def payDay(self, payout):
        self.balance = self.balance + payout


#player1 = goFishPlayer(1)
#player2 = goFishPlayer(2)
#player3 = goFishPlayer(3)
#player4 = goFishPlayer(4)
#player5 = goFishPlayer(5)

#goFishGame = goFish()
#goFishGame.playerList = [player1, player2, player3, player4, player5]
#goFishGame.playGame()
