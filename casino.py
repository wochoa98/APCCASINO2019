import random
import time
from array import *
from horse_racing.horse_racing import *
from roulette import *
from blackjack_class import *
from poker import *
from goFishNoPrint import *

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
        print ("Select what games you would like to run, minimum of 2 of the 5.")
        total = 0
        while total < 2:
            self.poker = eval(input("Do you want to run Poker? Yes[1]/No[0]: "))
            if self.poker == 1:
                self.pokerGame = poker()
                pokerVig = eval(input("What would you like the rake percent to be (write as decimal): "))
                self.pokerGame.rake = pokerVig
            self.blackjack = eval(input("Do you want to run Blackjack? Yes[1]/No[0]: "))
            if self.blackjack == 1:
                self.blackjackGame = blackjackGame()
                stand = eval(input("What is the dealer's hard stand value (Recommended 17): "))
                self.blackjackGame.DH2 = stand
                max = eval(input("What would you like the blackjack value to be (Recommended/Usually 21)?"))
                self.blackjackGame.bjNum = max
            self.fish = eval(input("Do you want to run Go Fish? Yes[1]/No[0]: "))
            if self.fish == 1:
                self.fishGame = goFish()
                fishVig = eval(input("What would you like the rake percent to be (write as decimal): "))
                self.fishGame.casinoP = fishVig
                #buyIn = eval(input("Do you want a high table minimum [1], an average table minimum [2], or a low table minimum [3]?: "))
                #set fishGame.tableMin = buyIn
            self.roulette = eval(input("Do you want to run roulette? Yes[1]/No[0]: "))
            if self.roulette == 1:
                self.rouletteGame = roulette()
                tableMin = eval(input("Do you want a high table minimum [1], an average table minimum [2], or a low table minimum [3]?: "))
                self.rouletteGame.tableM = tableMin
            self.horses = eval(input("Do you want to run horse betting? Yes[1]/No[0]: "))
            if self.horses == 1:
                accuracy = eval(input("Do you want the horse odd predictions to be very accurate [1], somewhat accurate [2], or innaccurate [3]: "))
                self.horseBetting = Race(accuracy)
            total = self.poker + self.blackjack + self.fish + self.roulette + self.horses
            if total < 2:
                print("I'm sorry, you didn't select enough games to run. Please try again.")
                self.poker = 0
                self.blackjack = 0
                self.fish = 0
                self.roulette = 0
                self.horses = 0
        self.rounds = eval(input("How many rounds would you like to run through?: "))


    def __init__(self):
        self.customers = [] #will be list of all active customers
        self.leaderboard = [] #will be static, holds player records whether active in casino or not
        #set up games
        self.simMenu()
        #for initial start there are 6 per active game
        if self.poker == 1: #first 6 players go to poker
            for i in range(6):
                newPlayer = player(len(self.customers))
                newPlayer.status = "Poker"
                self.pokerGame.playerList.append(newPlayer)
                self.customers.append(newPlayer) #added as active player
                self.leaderboard.append(newPlayer) #added to records
        if self.blackjack == 1: #second group of 6 play blackjack
            for i in range(6):
                newPlayer = player(len(self.customers))
                newPlayer.status = "Blackjack"
                self.blackjackGame.playerList.append(newPlayer)
                self.customers.append(newPlayer) #added as active player
                self.leaderboard.append(newPlayer) #added to records
        if self.fish == 1: #third group of 6 plays Go Fish
            for i in range(6):
                newPlayer = player(len(self.customers))
                newPlayer.status = "Go Fish"
                self.fishGame.playerList.append(newPlayer)
                self.customers.append(newPlayer) #added as active player
                self.leaderboard.append(newPlayer) #added to records
        if self.roulette == 1: #fourth group of 6 plays Roulette
            for i in range(6):
                newPlayer = player(len(self.customers))
                newPlayer.status = "Roulette"
                self.rouletteGame.playerList.append(newPlayer)
                self.customers.append(newPlayer) #added as active player
                self.leaderboard.append(newPlayer) #added to records
        if self.horses == 1:
            for i in range(6):
                newPlayer = player(len(self.customers))
                newPlayer.status = "Horse Betting"
                self.horseBetting.playerList.append(newPlayer)
                self.customers.append(newPlayer) #added as active player
        #for players in self.fishGame.playerList:
        #        if players.balance < 1000:
        #                self.fishGame.playerList.remove(players)
        #                self.customers.remove(players)
        #                for people in self.leaderboard:
        #                        if people == players:
        #                                people.status = "OOH"
        #                newPlayer = player(len(self.customers))
        #                newPlayer.status = "Go Fish"
        #                self.customers.append(newPlayer)
        #                self.leaderboard.append(newPlayer)
        #                self.fishGame.payerList.append(newPlayer)
        #                self.leaderboard.append(newPlayer) #added to records

    def playerControl(self):
        # run a check first for players that will not make minimums, check poker for struggling people who are being outbet, readd new players to fill void
        #make minimum money at a poker table 5k, every other game minimum is 1k, players leave their games if they have less than 1k at start of round
        #check poker first for 5k
        if self.poker == 1:
            for players in self.pokerGame.playerList:
                if players.balance < 5000:
                    self.pokerGame.playerList.remove(players) #removes from players and active customers, keeps record
                    self.customers.remove(players)
                    for people in self.leaderboard:
                        if people == players:
                            people.status == "OOH"
                    newPlayer = player(len(self.customers))
                    newPlayer.status = "Poker"
                    self.customers.append(newPlayer)
                    self.leaderboard.append(newPlayer)
                    self.pokerGame.playerList.append(newPlayer)
        #check each game for less than 1000 now
        if self.blackjack == 1:
            for players in self.blackjackGame.playerList:
                if players.balance < 1000:
                    self.blackjackGame.playerList.remove(players)
                    self.customers.remove(players)
                    for people in self.leaderboard:
                        if people == players:
                            people.status = "OOH"
                    newPlayer = player(len(self.customers))
                    newPlayer.status = "Blackjack"
                    self.customers.append(newPlayer)
                    self.leaderboard.append(newPlayer)
                    self.blackjackGame.playerList.append(newPlayer)
        if self.fish == 1:
            for players in self.fishGame.playerList:
                if players.balance < 1000:
                    self.fishGame.playerList.remove(players)
                    self.customers.remove(players)
                    for people in self.leaderboard:
                        if people == players:
                            people.status = "OOH"
                    newPlayer = player(len(self.customers))
                    newPlayer.status = "Go Fish"
                    self.customers.append(newPlayer)
                    self.leaderboard.append(newPlayer)
                    self.fishGame.payerList.append(newPlayer)
        if self.roulette == 1:
            for players in self.rouletteGame.playerList:
                if players.balance < 1000:
                    self.rouletteGame.playerList.remove(players)
                    self.customers.remove(players)
                    for people in self.leaderboard:
                        if people == players:
                            people.status == "OOH"
                    newPlayer = player(len(self.customers))
                    newPlayer.status = "Roulette"
                    self.customers.append(newPlayer)
                    self.leaderboard.append(newPlayer)
                    self.rouletteGame.playerList.append(newPlayer)
        if self.horses == 1:
            for players in self.horseBetting.playerList:
                if players.balance < 1000:
                    self.horseBetting.playerList.remove(players)
                    self.customers.remove(players)
                    for people in self.leaderboard:
                        if people == players:
                            people.status == "OOH"
                    newPlayer = player(len(self.customers))
                    newPlayer.status = "Horse Betting"
                    self.customers.append(newPlayer)
                    self.leaderboard.append(newPlayer)
                    self.horseBetting.playerList.append(newPlayer)
        playerAction = random.randint(1,4) # 1=addPlayer, 2=deletePlayer, 3=movePlayer, 4=noChange
        if playerAction == 1:
            player2add = player(len(self.customers))
            chosen = 0
            while chosen == 0:
                gameAdded = random.randint(1,5) #selects game randomly that it will append to
                if gameAdded == 1: # 1 will be poker
                    if self.poker == 1:
                        player2add.status = "Poker"
                        self.pokerGame.playerList.append(player2add) #added to poker player list
                        chosen = 1
                elif gameAdded == 2: # 2 will be blackjack
                    if self.blackjack == 1:
                        player2add.status = "Blackjack"
                        self.blackjackGame.playerList.append(player2add) #added to blackjack player list
                        chosen = 1
                elif gameAdded == 3: # 3 will be go fish
                    if self.fish == 1:
                        player2add.status = "Go Fish"
                        self.fishGame.playerList.append(player2add) #added to go fish player list
                        chosen = 1
                elif gameAdded == 4: # 4 will be roulette
                    if self.roulette = 1:
                        player2add.status = "Roulete"
                        self.rouletteGame.playerList.append(player2add) #added to the roulette player list
                        chosen = 1
                else: #5 was selected, 5 will be horse betting
                    if self.horses = 1:
                        player2add.status = "Horse Betting"
                        self.horseBetting.playerList.append(player2add) #added to the horse betting player list
                        chosen = 1
                        
            self.customers.append(player2add) #adds as active player to casino
            self.leaderboard.append(player2add) #adds player record to casino

        elif playerAction == 2:
            player2delete = random.randint(0,len(self.customers)-1) #list will already be filled, int will be 0 to the last customer
            gameAt = None
            for people in self.customers:

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
                        self.fishGame.playerList.remove(players)
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
            moved = 0
            player2move = random.randint(0,len(self.customers)-1)
            gameTo = random.randint(1,4) #player will have 4 possible games to join from the one they are leaving
            for people in self.customers:
                if people.playerNumber == player2move:
                    gameAt = people.status
                    if gameAt == "Poker":
                        for players in self.pokerGame.playerList:
                            if players.playerNumber == player2move:
                                playerMoving = players
                                self.pokerGame.playerList.remove(players)
                                while moved == 0:
                                    if gameTo == 1: #poker to blackjack
                                        if self.blackjack == 1:
                                            playerMoving.status = "Blackjack" #will this change the values in customer/leaderboard
                                            self.blackjackGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 2: #poker to Go fish
                                        if self.fish == 1:
                                            playerMoving.status = "Go Fish"
                                            self.fishGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 3: #poker to roulette
                                        if self.roulette == 1:
                                            playerMoving.status = "Roulette"
                                            self.rouletteGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    else: #poker to horse betting
                                        if self.horses == 1:
                                            playerMoving.status = "Horse Betting"
                                            self.horseBetting.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                    elif gameAt == "Blackjack":
                        for players in self.blackjackGame.playerList:
                            if players.playerNumber == player2move:
                                playerMoving = players
                                self.blackjackGame.playerList.remove(players)
                                while moved == 0:
                                    if gameTo == 1: #blackjack to poker
                                        if self.poker == 1:
                                            playerMoving.status = "Poker"
                                            self.pokerGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 2: #blackjack to Go Fish
                                        if self.fish == 1:
                                            playerMoving.status = "Go Fish"
                                            self.fishGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 3: #blackjack to roulette
                                        if self.roulette == 1:
                                            playerMoving.status = "Roulette"
                                            self.rouletteGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    else: #blackjack to horse betting
                                        if self.horses == 1:
                                            playerMoving.status = "Horse Betting"
                                            self.horseBetting.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                    elif gameAt == "Go Fish":
                        for players in self.fishGame.playerList:
                            if players.playerNumber == player2move:
                                playerMoving = players
                                self.fishGame.playerList.remove(players)
                                while moved == 0:
                                    if gameTo == 1: #go fish to poker
                                        if self.poker == 1:
                                            playerMoving.status == "Poker"
                                            self.pokerGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 2: #go fish to blackjack
                                        if self.blackjack == 1:
                                            playerMoving.status = "Blackjack"
                                            self.blackjackGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 3: #go fish to Roulette
                                        if self.roulette == 1:
                                            playerMoving.status = "Roulette"
                                            self.rouletteGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    else: #go fish to Horse Betting
                                        if self.horses == 1:
                                            playerMoving.status = "Horse Betting"
                                            self.horseBetting.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                    elif gameAt == "Roulette":
                        for players in self.rouletteGame.playerList:
                            if players.playerNumber == player2move:
                                playerMoving = players
                                self.rouletteGame.playerList.remove(players)
                                while moved == 0:
                                    if gameTo == 1: #roulette to poker
                                        if self.poker == 1:
                                            playerMoving.status == "Poker"
                                            self.pokerGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 2: #roulette to blackjack
                                        if self.blackjack == 1:
                                            playerMoving.status = "Blackjack"
                                            self.blackjackGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 3: #roulette to go fish
                                        if self.fish == 1:
                                            playerMoving.status = "Go Fish"
                                            self.fishGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    else: #go fish to Horse Betting
                                        if self.horses == 1:
                                            playerMoving.status = "Horse Betting"
                                            self.horseBetting.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                    elif gameAt == "Horse Betting":
                        for players in self.horseBetting.playerList:
                            if players.playerNumber == player2move:
                                playerMoving = players
                                self.horseBetting.playerList.remove(players)
                                while moved == 0:
                                    if gameTo == 1: #horse betting to poker
                                        if self.poker == 1:
                                            playerMoving.status == "Poker"
                                            self.pokerGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 2: #horse betting to blackjack
                                        if self.blackjack == 1:
                                            playerMoving.status = "Blackjack"
                                            self.blackjackGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    elif gameTo == 3: #horse betting to Roulette
                                        if self.roulette == 1:
                                            playerMoving.status = "Roulette"
                                            self.rouletteGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                                    else: #horse betting to go fish
                                        if self.fish == 1:
                                            playerMoving.status = "Go Fish"
                                            self.fishGame.playerList.append(playerMoving)
                                            moved = 1
                                        else:
                                            gameTo = random.randint(1,4)
                    for people in self.customers:
                        if people.playerNumber == player2move:
                            people.status == playerMoving.status
                    for people in self.leaderboard:
                        if people.playerNumber == player2move:
                            people.status == playerMoving.status


    def updateBoards(self):
        if self.poker == 1:
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
        if self.blackjack == 1:
            for people in self.blackjackGame.playerList:
                people.plusMinus = people.balance - people.startingBalance
                for custs in self.customers:
                    if people.playerNumber == custs.playerNumber:
                        custs.balance = people.balance
                        custs.plusMinus = people.plusMinus
                for leaders in self.leaderboard:
                    if people.playerNumber == leaders.playerNumber:
                        leaders.balance = people.balance
                        leaders.plusMinus = people.plusMinus
        if self.fish == 1:
            for people in self.fishGame.playerList:
                people.plusMinus = people.balance - people.startingBalance
                for custs in self.customers:
                    if people.playerNumber == custs.playerNumber:
                        custs.balance = people.balance
                        custs.plusMinus = people.plusMinus
                for leaders in self.leaderboard:
                    if people.playerNumber == leaders.playerNumber:
                        leaders.balance = people.balance
                        leaders.plusMinus = people.plusMinus
        if self.roulette == 1:
            for people in self.rouletteGame.playerList:
                people.plusMinus = people.balance - people.startingBalance
                for custs in self.customers:
                    if people.playerNumber == custs.playerNumber:
                        custs.balance = people.balance
                        custs.plusMinus = people.plusMinus
                for leaders in self.leaderboard:
                    if people.playerNumber == leaders.playerNumber:
                        leaders.balance = people.balance
                        leaders.plusMinus = people.plusMinus
        if self.horses == 1:
            for people in self.horseBetting.playerList:
                people.plusMinus = people.balance - people.startingBalance
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
                self.blackjackGame.blackjackgame()
            if self.fish == 1:
                self.fishGame.playGame()
            if self.roulette == 1:
                self.rouletteGame.playRound()
            if self.horses == 1:
                self.horseBetting.playRound()
                self.updateBoards()
            self.playerControl()

    def printStats(self):
        if self.poker == 1:
            self.profit = self.profit + self.pokerGame.casinoWinnings
        if self.blackjack == 1:
            self.profit = self.profit + self.blackjackGame.bjWinnings
        if self.fish == 1:
            self.profit = self.profit + self.fishGame.winnings
        if self.roulette == 1:
            self.profit = self.profit + self.rouletteGame.casinoWinnings
        if self.horses == 1:
            self.profit = self.profit + self.horseBetting.casinoWinnings
        #poker
        print("Poker Stats:")
        print("     Casino Winnings from Poker: $", self.pokerGame.casinoWinnings)
        pokerPercent = (self.pokerGame.casinoWinnings/self.profit) * 100 #percent profit from poker
        print("       Percent:", pokerPercent, "%")
        averageAnte = (self.pokerGame.casinoWinnings /self.pokerGame.rake) / self.rounds #casino winnings = ante * rake => ante = casino winnings/rake, divide by rounds to find average
        print("     Average Ante: $", averageAnte, end=' ')
        print("     Rake Percent:", (self.pokerGame.rake * 100),"%")
        #blackjack
        print("Blackjack Stats:")
        print("     Casino Winnings from Blackjack: $", self.blackjackGame.bjWinnings)
        bjPercent = (self.blackjackGame.bjWinnings/self.profit) * 100 #percent profit from blackjack
        print("       Percent:", bjPercent, "%")
        #calculate average bet?
        print("     Dealer Hard Stand:", self.blackjackGame.DH2)
        #calculate times dealer busts based on hard stand value?
        #Go Fish
        print("Go Fish Stats:")
        print("     Casino winnings from Go Fish: $", self.fishGame.winnings)
        fishPercent = (self.fishGame.winnings/self.profit) * 100 #percent profit from Go Fish
        print("       Percent:", fishPercent, "%")
        #print("     Table Vig:", self.fishGame.vig, "%")
            ## Other Fish Stats?
        #roulette
        print("Roulette Stats:")
        print("     Casino Winnings from Roulette: $", self.rouletteGame.casinoWinnings)
        roulettePercent = (self.rouletteGame.casinoWinnings/self.profit) * 100 #percent profit from Roulette
        print("       Percent:", roulettePercent, "%")
        print("     Table Minimum: $", self.rouletteGame.tableMin)
            ## player win rate?
        #horse betting
        print("Horse Betting Stats:")
        print("     Casino Winnings from Horse Betting: $", self.horseBetting.casinoWinnings)
        horsePercent = (self.horseBetting.casinoWinnings/self.profit) * 100 #percent profit from horse betting
        print("       Percent:", horsePercent, "%")
        print("     Accuracy of Odds:", self.horseBetting.prob_entropy, "%")
            ## player win rate from odds

    def printPlayer(self, index):
        print("Player Number:", self.leaderboard[index].playerNumber)
        print("Overall Winnings:", self.leaderboard[index].plusMinus)
        print("Player Type:", self.leaderboard[index].playType)
        print("Player Status:", self.leaderboard[index].status)

    def printLeaderboard(self):
        for people in self.leaderboard:
            people.plusMinus = people.balance - people.startingBalance #sets all players final over/under of starting balance
            self.leaderboard.sort(key = lambda x: x.plusMinus, reverse=True) #will sort leaderboard based on the final over/under of starting balance
        for i in range(len(self.leaderboard)):
            if i == 0: #top player of the "night" (1 full simulation)
                print("======= Top Whales =======")
                print("The top whale of the night was:")
                self.printPlayer(i)
            elif i == 1: #second player
                print("The second place player of the night was:")
                self.printPlayer(i)
            elif i == 2: #third player
                print("The third place player of the night was:")
                self.printPlayer(i)
                print("==========================")
            elif i == len(self.leaderboard) - 3: #third worst player
                print("====== Bottom Fish ======")
                print("The third worst player of the night was:")
                self.printPlayer(i)
            elif i == len(self.leaderboard) - 2:
                print("The second worst player of the night was:")
                self.printPlayer(i)
            elif i == len(self.leaderboard) -1 : #worst player
                print("The fish of the night was:")
                self.printPlayer(i)
                print("=========================")
            #else: #any player in the middle
                #self.printPlayer(i)

    def play(self):
        print("Welcome to the Casino Simulator")
        while self.quit != 1:
            self.runCasino()
            self.printStats()
            self.printLeaderboard()
            choice = eval(input("Would you like to run another simulation? Yes[1]/No[0]: "))
            if choice != 1:
                self.quit = 1
                print("Thank you for playing.")

class hand:
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
            #print "Card:", self.cValues[a], "Suit:", self.sValues[a]

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
        #print "Player has hand value", self.handValue, "after checking for flushes"

    def hasStraight(self):
        self.cValues.sort()
        low = min(self.cValues)
        if (low + 1 in self.cValues) and (low + 2 in self.cValues) and (low + 3 in self.cValues) and (low + 4 in self.cValues): # if straight
            self.handValue = 5
            self.highCard = (low + 4)
        #print "Player has hand value", self.handValue, "after checking straight"

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

    def hasPair(self):
        self.cValues.sort()
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


    def setHighCard(self):
        if self.cValues[0] == 1:
            self.highCard = 1
            self.handValue = 1
        else:
            self.highCard = self.cValues[4]
            self.handValue = 1


class player:
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
    toat = 0 #blackjack
    hand = []
    final = 0
    win = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0

    def __init__(self, num):
        self.playerNumber = num
        self.balance = random.randint(40000, 55000)
        self.startingBalance = self.balance
        self.playType = random.randint(1,3)
        self.localHand = hand(num)
        self.playerHand = []
        self.matches = 0
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
        if self.bluff == 20:
            self.bluff = 1
            betPer = random.randint(15,25) #bluff bets 15 to 25 percent on first bet
            self.bet = betPer * newCasino.pokerGame.ante / 100
            return self.bet
        if self.localHand.handValue == 1: #player has high card
            if self.playType == 1:
                self.fold = 1
                self.bet = 0
                return 0 #returning a 0 will be a fold, player type 1 folds on high card for safety
            else:
                betPer = random.randint(4,6) #player type 2 and 3 bet 4 to 6 percent on hgih card hands
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 2: #player has pair
            if self.playType == 1:
                betPer = random.randint(4,6) #player type 1 will bet 4 to 6%
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(3,7) #player type 2 and 3 will bet 3 to 7 percent on a pair
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 3: #player has 2 pair
            if self.playType == 1:
                betPer = random.randint(4,6) #player type 1 betse 4 to 6 percent on 2 pair
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(6,10) #player type 2 and 3 bet 6 to 10 percent on 2 pair
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 4: #player has 3 of a kind
            if self.playType == 1:
                betPer = random.randint(7,9) #plaer type 1 only bets 7 to 9 percent on 3 of a kind
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(7, 13) #player type 2 and 3 will bet 7 to 13 percent on 3 of a kind
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 5: #player has a Straight
            if self.playType == 1:
                betPer = random.randint(7,9) #player type 1 will bet 7 to 9 percent on a straight
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(7,13) #player type 2 and 3 will bet 7 to 13 percent on a straight
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 6: #player has flush
            if self.playType == 1:
                betPer = random.randint(8,12) #player type 1 will bet 8 to 12 percent on a flush
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(10,20) #player type 2 and 3 will bet 10 to 20 percent on a flush
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 7: #player has full house
            if self.playType == 1:
                betPer = random.randint(13,17) #player type 1 will bet 13 to 17 % on a full house
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(10,20) #player type 2 nd 3 will bet 10 to 20 percent on a full house
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 8: #player has 4 of a kind
            if self.playType == 1:
                betPer = random.randint(18,22) #player type 1 bets 18 to 22 percent on 4 of a kind
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(10,20) #player 2 and 3 bet 10 to 20 percent on 4 of a kind
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        elif self.localHand.handValue == 9: #player has a straight flush
            if self.playType == 1:
                betPer = random.randint(18,22) #player 1 bets 18 to 22 percent on a straight flush
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            else:
                betPer = random.randint(15,25) #player type 2 and 3 bets 15 to 25 percent on straight flush
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
        else: #player has royal flush
            if self.playType == 1:
                self.bet = newCasino.pokerGame.ante #player type 1 goes all in on royal flush
                return self.bet
            else:
                betPer = random.randint(15,25) #player type 2 and 3 bets 15 to 25 percent on royal flush
                self.bet = betPer * newCasino.pokerGame.ante / 100
                return self.bet
            
    def dealStart(self):
        self.hand = []
        for i in range(2):
            deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
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

    def placeBet2(self):
        if self.bluff == 1:
            betPer = random.randint(25,35) #bluff bets 25 to 35 percent on bet
            self.bet2 = betPer * newCasino.pokerGame.ante / 100
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
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 2: #player has pair
            if self.playType == 1:
                betPer = random.randint(4,6) #player type 1 will bet 4 to 6%
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(3,7) #player type 2 and 3 will bet 3 to 7 percent on a pair
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 3: #player has 2 pair
            if self.playType == 1:
                betPer = random.randint(4,6) #player type 1 betse 4 to 6 percent on 2 pair
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(6,10) #player type 2 and 3 bet 6 to 10 percent on 2 pair
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 4: #player has 3 of a kind
            if self.playType == 1:
                betPer = random.randint(7,9) #plaer type 1 only bets 7 to 9 percent on 3 of a kind
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(7, 13) #player type 2 and 3 will bet 7 to 13 percent on 3 of a kind
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 5: #player has a Straight
            if self.playType == 1:
                betPer = random.randint(7,9) #player type 1 will bet 7 to 9 percent on a straight
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(12,18) #player type 2 and 3 will bet 12 to 19 percent on a straight
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 6: #player has flush
            if self.playType == 1:
                betPer = random.randint(8,12) #player type 1 will bet 8 to 12 percent on a flush
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(15,25) #player type 2 and 3 will bet 15 to 25 percent on a flush
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 7: #player has full house
            if self.playType == 1:
                betPer = random.randint(13,17) #player type 1 will bet 13 to 17 % on a full house
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(15,25) #player type 2 nd 3 will bet 15 to 25 percent on a full house
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 8: #player has 4 of a kind
            if self.playType == 1:
                betPer = random.randint(18,22) #player type 1 bets 18 to 22 percent on 4 of a kind
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(20,30) #player 2 and 3 bet 20 to 30 percent on 4 of a kind
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        elif self.localHand.handValue == 9: #player has a straight flush
            if self.playerType == 1:
                betPer = random.randint(18,22) #player 1 bets 18 to 22 percent on a straight flush
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
            else:
                betPer = random.randint(20,30) #player type 2 and 3 bets 20 to 30 percent on straight flush
                self.bet2 = betPer * newCasino.pokerGame.ante / 100
                return self.bet2
        else: #player has royal flush
            if self.playType == 1:
                self.bet2 = newCasino.pokerGame.ante #player type 1 goes all in on royal flush
                return self.bet2
            else:
                self.bet2 = self.balance
                self.allIn = 1
                return self.bet2

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


                                            self.matches += 1
                                            return
                                    return
                            return
                    return
            return

    def askRand(self):
        if(len(self.playerHand) > 0):
            randCard = random.randint(0, len(self.playerHand)-1)
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
newCasino = casino()
newCasino.play()
