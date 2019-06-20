'''
Roulette Game
Nick Krysko and Matthew Alves
'''
from array import *
import random

random.seed(a = None, version = 2)

#class of bet type??

#expectedvalue = (1/n)(36-n) where n=# of pockets in wheel



while True:
    userBetType = eval(input("Enter number\n"))
    if userBetType == 1: #straight/single
        userNum = eval(input("Enter the pocket number\n"))
        x = random.randint(0,36)
        if userNum == x:
            print("Win!\n")
            #subtract user winnings from casino earnings
        else
            print("Loss.\n")
            #add bet amount to casino earnings
        break
    elif userBetType == 2: #split
        x = random.randint(0,36)
        print(x)
    elif userBetType == 3: #street
        do thing
    elif userBetType == 4: #corner/square
        do thing
    elif userBetType == 5: #six line / double street
        do thing
    elif userBetType == 6: #Trio
        do thing
    elif userBetType == 7: #first four
        do thing
    elif userBetType == 8: #basket
        do thing
    elif userBetType == 9: #outside bet Low
        do thing
    elif userBetType == 10: #outside bet high
        do thing
    elif userBetType == 11: #red / black
        do thing
    elif userBetType == 12: #even / odd
        do thing
    elif userBetType == 13: #dozen bet
        do thing
    elif userBetType == 14: #column bet
        do thing
    elif userBetType == 15: #snake basket
        do thing
    else:
        print("Invalid choice\n")


#take bet type
#take bet ammount
#calculate odds
#return win/loss
