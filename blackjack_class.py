import random
class blackjackGame:


        def __init__(self):
                self.bjNum = 21
                self.DH2 = 16
                self.playerList = []
                self.dealer0 = dealer()
                self.playerList = []

        
        deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        bjTempPot = 50000
        bjWinnings = bjTempPot - 50000


        def takeBets(self):
                for i in self.playerList:
                        i.balance = i.balance - 1000
                        self.bjTempPot += 1000
        
        def payout(self):
                for i in self.playerList:
                        if i.win == 3:
                                i.balance = i.balance + 2500
                                self.bjTempPot = self.bjTempPot - 2500
                        elif i.win == 2:
                                i.balance = i.balance + 1000
                                self.bjTempPot = self.bjTempPot -1000
                        elif i.win == 1:
                                i.balance = i.balance + 2000
                                self.bjTempPot = self.bjTempPot - 2000

        def dealHand(self):
                for i in self.playerList:
                        i.dealStart()
                self.dealer0.dealStart()


        def play(self, i):
                if i.playType == 1:
                        i.total()
                        done = 1
                        if i.toat == self.bjNum:
                                i.final = i.toat
                                i.win = 3
                                done = 0
                        while(done):
                                if i.toat >= 0 and i.toat <= 14:
                                        card = random.choice(self.deck)
                                        i.hand.append(card)
                                        i.total()
                                elif i.toat >= 15 and i.toat <= 16:
                                        hit = random.randint(0, 1)
                                        if hit == 0:
                                                i.final=i.toat
                                                done = 0
                                        elif hit == 1:
                                                card = random.choice(self.deck)
                                                i.hand.append(card)
                                                i.total()
                                elif i.toat >= 17 and i.toat <= self.bjNum:
                                        i.final = i.toat
                                        done = 0
                                elif i.toat > self.bjNum:
                                        i.final = -1
                                        done = 0
                elif i.playType == 2:
                        i.total()
                        done = 1
                        if i.toat == self.bjNum:
                                i.final = i.toat
                                i.win = 3
                                done = 0
                        while(done):
                                if i.toat >= 0 and i.toat <= 11:
                                        card = random.choice(self.deck)
                                        i.hand.append(card)
                                        i.total()
                                elif i.toat >= 11 and i.toat <= 15:
                                        hit = random.randint(0, 3)
                                        if hit < 1:
                                                i.final = i.toat
                                                done = 0
                                        elif hit >= 1:
                                                card = random.choice(self.deck)
                                                i.hand.append(card)
                                                i.total()
                                elif i.toat >= 15 and i.toat <= self.bjNum:
                                        i.final = i.toat
                                        done = 0
                                elif i.toat > self.bjNum:
                                        i.final = -1
                                        done = 0
                elif i.playType == 3:
                        i.total()
                        done = 1
                        if i.toat == self.bjNum:
                                i.final = i.toat
                                i.win = 3
                                done = 0
                        while(done):
                                if i.toat >= 0 and i.toat <= 11:
                                        card = random.choice(self.deck)
                                        i.hand.append(card)
                                        i.total()
                                elif i.toat >= 11 and i.toat <= 13:
                                        hit = random.randint(0, 8)
                                        if hit < 1:
                                                i.final = i.toat
                                                done = 0
                                        elif hit >= 1:
                                                card = random.choice(self.deck)
                                                i.hand.append(card)
                                                i.total()
                                elif i.toat >= 13 and i.toat <= self.bjNum:
                                        i.final = i.toat
                                        done = 0
                                elif i.toat > self.bjNum:
                                        i.final = -1
                                        done = 0
        def playDealer(self, dealer):
                if dealer.playType == 4:
                        dealer.total()
                        done = 1
                        if dealer.toat == self.bjNum:
                                dealer.final = dealer.toat
                                done = 0
                        while(done):
                                if dealer.toat >=0 and dealer.toat < self.DH2:
                                        card = random.choice(self.deck)
                                        dealer.hand.append(card)
                                        dealer.total()
                                elif dealer.toat >= self.DH2 and dealer.toat <= self.bjNum:
                                        dealer.final = dealer.toat
                                        done = 0
                                elif dealer.toat > self.bjNum:
                                        dealer.final = -1
                                        done = 0

        def blackjackgame(self):
                done = 1
                while(done):
                        choice = 1
                        ntb = 0
                        if choice == 1:
                                self.takeBets()
                                self.dealHand()
                                for i in self.playerList:
                                        self.play(i)
                                self.playDealer(self.dealer0)
                                self.dealer0.final = ntb
                                for i in self.playerList:
                                        if i.win == 0:
                                                if i.final == ntb:
                                                        i.win = 2
                                                elif i.final > ntb:
                                                        i.win = 1
                                                elif i.final < ntb:
                                                        i.win = 0
                                self.payout()
                                for i in self.playerList:
                                        i.toat=0
                                        i.final=0
                                        i.win=0
                                        i.hand=[]
                                self.dealer0.toat=0
                                self.dealer0.final=0
                                self.dealer0.win=0
                                self.dealer0.hand=[]
                                done = 0

class dealer:
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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
                    card = random.choice(self.deck)
                    self.hand.append(card)


    def total(self):
            for i in self.hand:
                    if i == 'A' and self.toat<=10:
                            self.toat+=11
                    elif i == 'A' and self.toat>=11:
                            self.toat+=1
                    else:
                            self.toat+=i
