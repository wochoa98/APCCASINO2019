from array import *
import copy
import random

#Go-Fish - Wilson Ochoa




class gameDeck:
	#cardValue = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13])
	#cardSuit = array('i', [1,2,3,4]) #1 = hearts, 2 = clubs, 3 = diamonds, 4 = spades
	
	
	def __init__(self):
		self.deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]  #0-12 = A-K Hearts || 13-25 = A-K Clubs || 26-38 = A-K Diamonds || 39-51 = A-K Spades
		self.cardsLeft = len(self.deck)
		self.gameEnd = 0
		
	def dealHands(self, p1, p2, p3, p4):
		p = 0
		for p in range(4):
			if(p1.getPresent() == 1):
				cardNum = random.randint(0, len(self.deck)-1)
				p1.addCard(self.deck[cardNum])
				self.deck.pop(cardNum)

			if(p2.getPresent() == 1):
				cardNum = random.randint(0, len(self.deck)-1)
				p2.addCard(self.deck[cardNum])
				self.deck.pop(cardNum)
				
			if(p3.getPresent() == 1):
				cardNum = random.randint(0, len(self.deck)-1)
				p3.addCard(self.deck[cardNum])
				self.deck.pop(cardNum)
				
			if(p4.getPresent() == 1):
				cardNum = random.randint(0, len(self.deck)-1)
				p4.addCard(self.deck[cardNum])
				self.deck.pop(cardNum)
			

	def resetDeck(self):
		self.deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
		
	def refill(self, p1, p2, p3, p4):
		if(len(self.deck) > 0):
			if(len(p1.playerHand) <= 3):
				temp = 4 - len(p1.playerHand)
				for i in range(temp):
					if(len(self.deck) > 0):
						cardNum = random.randint(0, len(self.deck)-1)
						p1.addCard(self.deck[cardNum])
						self.deck.pop(cardNum)
					else:
						return
			
			if(len(p2.playerHand) <= 3):
				temp = 4 - len(p2.playerHand)
				for i in range(temp):
					if(len(self.deck) > 0):
						cardNum = random.randint(0, len(self.deck)-1)
						p2.addCard(self.deck[cardNum])
						self.deck.pop(cardNum)
					else:
						return
					
			if(len(p3.playerHand) <= 3):
				temp = 4 - len(p3.playerHand)
				for i in range(temp):
					if(len(self.deck) > 0):
						cardNum = random.randint(0, len(self.deck)-1)
						p3.addCard(self.deck[cardNum])
						self.deck.pop(cardNum)
					else:
						return
					
			if(len(p4.playerHand) <= 3):
				temp = 4 - len(p4.playerHand)
				for i in range(temp):
					if(len(self.deck) > 0):
						cardNum = random.randint(0, len(self.deck)-1)
						p4.addCard(self.deck[cardNum])
						self.deck.pop(cardNum)
					else:
						return
				
	def sortCards(self, p1, p2, p3, p4):
		if(len(p1.playerHand) > 0):
			p1.playerHand.sort()
		
		if(len(p2.playerHand) > 0):
			p2.playerHand.sort()
			
		if(len(p3.playerHand) > 0):
			p3.playerHand.sort()
			
		if(len(p4.playerHand) > 0):
			p4.playerHand.sort()
			
			
	def checkGameEnd(self, p1, p2, p3, p4):
		if(len(self.deck) == 0):
			if(len(p1.playerHand) == 0):
				self.gameEnd = self.gameEnd + p1.getPresent()
				p1.playerLeave()
				
			if(len(p2.playerHand) == 0):
				self.gameEnd = self.gameEnd + p2.getPresent()
				p2.playerLeave()
				
			if(len(p3.playerHand) == 0):
				self.gameEnd = self.gameEnd + p3.getPresent()
				p3.playerLeave()
				
			if(len(p4.playerHand) == 0):
				self.gameEnd = self.gameEnd + p4.getPresent()
				p4.playerLeave()
			
			
			
	



class goFishPlayer:
	
	def __init__(self):
		self.playerHand = []
		self.handSize = len(self.playerHand)
		self.matches = 0
		self.playerPresent = 0
		self.wins = 0
	
	
	def checkMatch(self):
		if(len(self.playerHand) >= 4):
			cardCount = 0
			for i in range(len(self.playerHand)):
				
				if((self.playerHand[i] >= 0) & (self.playerHand[i] <= 12)):
					cardCount = cardCount + 1
					print("m", i)
					
					for a in range(len(self.playerHand)):
						if(self.playerHand[a] == self.playerHand[i] + 13):
							cardCount = cardCount + 1
							print("a", a)
							
							for b in range(len(self.playerHand)):
								if(self.playerHand[b] == self.playerHand[i] + 26):
									cardCount = cardCount + 1
									print("t", b)
									
									for c in range(len(self.playerHand)):	
										if(self.playerHand[c] == self.playerHand[i] + 39):
											print("ch", c)
											
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
						print("Given : ", temp)					
						print("New Hand : ", p.playerHand)
						return
						
					elif(h == len(self.playerHand)-1):
						p.goFish(d)
						
					
				elif((c >= 13) & (c <= 25)):
					if((self.playerHand[h] == c - 13)|(self.playerHand[h] == c + 13)|(self.playerHand[h] == c + 26)):
						temp = [elem if elem == (c-13) else elem if elem == (c+13) else elem if elem == (c+26) else 100 for elem in self.playerHand]
						temp = [elem for elem in temp if elem != 100]
						self.playerHand = [elem for elem in self.playerHand if elem not in temp]
						p.playerHand.extend(temp)
						print("Given : ", temp)					
						print("New Hand : ", p.playerHand)
						return
						
					elif(h == len(self.playerHand)-1):
						p.goFish(d)
				
				elif((c >= 26) & (c <= 38)):
					if((self.playerHand[h] == c - 26)|(self.playerHand[h] == c - 13)|(self.playerHand[h] == c + 13)):
						temp = [elem if elem == (c-26) else elem if elem == (c-13) else elem if elem == (c+13) else 100 for elem in self.playerHand]
						temp = [elem for elem in temp if elem != 100]
						self.playerHand = [elem for elem in self.playerHand if elem not in temp]
						p.playerHand.extend(temp)
						print("Given : ", temp)					
						print("New Hand : ", p.playerHand)
						return
						
					elif(h == len(self.playerHand)-1):
						p.goFish(d)

				elif(c >= 39):
					if((self.playerHand[h] == c - 39)|(self.playerHand[h] == c - 26)|(self.playerHand[h] == c - 13)):
						temp = [elem if elem == (c-39) else elem if elem == (c-26) else elem if elem == (c-13) else 100 for elem in self.playerHand]
						temp = [elem for elem in temp if elem != 100]
						self.playerHand = [elem for elem in self.playerHand if elem not in temp]
						p.playerHand.extend(temp)
						print("Given : ", temp)					
						print("New Hand : ", p.playerHand)
						return
						
					elif(h == len(self.playerHand)-1):
						p.goFish(d)
			
			
	def getPresent(self):
		return self.playerPresent
		
	def setPresent(self):
		self.playerPresent = 1
		
	def	playerLeave(self):
		self.playerPresent = 0
	
	def addCard(self, card):
		self.playerHand.append(card)
	
	def goFish(self, d):
		if(len(d.deck) > 0):
			cardNum = random.randint(0, len(d.deck)-1)
			self.addCard(d.deck[cardNum])
			d.deck.pop(cardNum)	
			print("Go-Fish!")
	def resetHand(self):
		self.playerHand = []
		self.matches = 0












gameEnd = 0
inGameDeck = gameDeck()
player1 = goFishPlayer()
player2 = goFishPlayer()
player3 = goFishPlayer()
player4 = goFishPlayer()

player1.setPresent()
player2.setPresent()
player3.setPresent()
player4.setPresent()
askedCard = 0
for i in range(1):
	inGameDeck.dealHands(player1, player2, player3, player4)
	print(player1.playerHand)
	print(player2.playerHand)
	print(player3.playerHand)
	print(player4.playerHand)
	round = 1
	
	inGameDeck.sortCards(player1, player2, player3, player4)
	while inGameDeck.gameEnd  < 4:
		
		inGameDeck.checkGameEnd(player1, player2, player3, player4)
		
		print("Round : ", round)
		print("")
		
		#Player 1's turn
		
		inGameDeck.sortCards(player1, player2, player3, player4)
		
		print("P1 Hand :", player1.playerHand)
		
		if(len(player1.playerHand) != 0):
			randPlayer = random.randint(0, 2)
			askedCard = player1.askRand()
			print("Asked - ", randPlayer)

			if(randPlayer == 0):
				player2.askedPlayer(player1, askedCard, inGameDeck)
				
			elif(randPlayer == 1):
				player3.askedPlayer(player1, askedCard, inGameDeck)
			
			elif(randPlayer == 2):
				player4.askedPlayer(player1, askedCard, inGameDeck)
			
			inGameDeck.checkGameEnd(player1, player2, player3, player4)
			inGameDeck.sortCards(player1, player2, player3, player4)
			player1.checkMatch()
			
			
		inGameDeck.refill(player1, player2, player3, player4)
		
		
		print("Player 1 Matches : ", player1.matches)
		
		#Player 2's turn
		
		inGameDeck.sortCards(player1, player2, player3, player4)
		
		print("P2 Hand :", player2.playerHand)
		
		if(len(player2.playerHand) != 0):
			randPlayer = random.randint(0, 2)
			askedCard = player2.askRand()
			print("Asked - ", randPlayer)
			
			
			if(randPlayer == 0):
				player1.askedPlayer(player2, askedCard, inGameDeck)
				
			elif(randPlayer == 1):
				player3.askedPlayer(player2, askedCard, inGameDeck)
			
			elif(randPlayer == 2):
				player4.askedPlayer(player2, askedCard, inGameDeck)
			
			inGameDeck.checkGameEnd(player1, player2, player3, player4)
			inGameDeck.sortCards(player1, player2, player3, player4)
			player2.checkMatch()
		
		inGameDeck.refill(player1, player2, player3, player4)
		
		
		print("Player 2 Matches : ", player2.matches)
		
		#Player 3's turn
		
		inGameDeck.sortCards(player1, player2, player3, player4)
		
		print("P3 Hand :", player3.playerHand)
		
		if(len(player3.playerHand) != 0):	
			randPlayer = random.randint(0, 2)
			askedCard = player3.askRand()
			print("Asked - ", randPlayer)

			if(randPlayer == 0):
				player1.askedPlayer(player3, askedCard, inGameDeck)
				
			elif(randPlayer == 1):
				player2.askedPlayer(player3, askedCard, inGameDeck)
			
			elif(randPlayer == 2):
				player4.askedPlayer(player3, askedCard, inGameDeck)
			
			inGameDeck.checkGameEnd(player1, player2, player3, player4)
			inGameDeck.sortCards(player1, player2, player3, player4)
			player3.checkMatch()
		
		inGameDeck.refill(player1, player2, player3, player4)
		
		
		print("Player 3 Matches : ", player3.matches)
		
		#Player 4's turn
		
		inGameDeck.sortCards(player1, player2, player3, player4)

		print("P4 Hand :", player4.playerHand)
		
		if(len(player4.playerHand) != 0):
			randPlayer = random.randint(0, 2)
			askedCard = player4.askRand()
			print("Asked - ", randPlayer)

			if(randPlayer == 0):
				player1.askedPlayer(player4, askedCard, inGameDeck)
				
			elif(randPlayer == 1):
				player2.askedPlayer(player4, askedCard, inGameDeck)
			
			elif(randPlayer == 2):
				player3.askedPlayer(player4, askedCard, inGameDeck)
			
			inGameDeck.checkGameEnd(player1, player2, player3, player4)
			inGameDeck.sortCards(player1, player2, player3, player4)
			player4.checkMatch()
		
		inGameDeck.refill(player1, player2, player3, player4)

		
		print("Player 4 Matches : ", player4.matches)
		
		print(inGameDeck.deck)
		round = round + 1
		
		i = i + 1
		
	inGameDeck.resetDeck()
	
	player1.resetHand()
	player2.resetHand()
	player3.resetHand()
	player4.resetHand()

