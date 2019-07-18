import random, time

straight_up = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
first_dozen = [1,2,3,4,5,6,7,8,9,10,11,12]
second_dozen = [13,14,15,16,17,18,19,20,21,22,23,24]
third_dozen = [25,26,27,28,29,30,31,32,33,34,35,36]
first_column = [1,4,7,10,13,16,19,22,25,28,31,43]
second_column = [2,5,8,11,14,17,20,23,26,29,32,35]
third_column = [3,6,9,12,15,18,21,24,27,30,33,36]
lower_half = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
upper_half = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
corner = [[1,2,4,5],[2,3,5,6],[4,5,7,8],[5,6,8,9]]
street = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30],[31,32,33],[34,35,36]]
line = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
split = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] #too many combinations -> use user input to check
basket = [0,1,2,3]

menu_choices = [0, 1, 2]
choices = ['L','E','R','B','O','U','4','5','6','0']
choices2 = ['C','S','T','I','Q','0']

def roll():
    return random.choice(straight_up)
result = roll()

table_minimum = 10
player_money = 50
player_bet = 0
'''
for i in range(100):
    print(roll())
'''
def printmenu():
    print(40*'-')
    print("Welcome Player to Roulette")
    print("Press 1 to make an outside bet")
    print("Press 2 to make an inside bet")
    print("Press 0 to exit")
    print(40*'-'+ '\n')
    
def spin_phrase():
    print("The dealer is now spinning the wheel")
    time.sleep(1)
    print("The ball lands on number", result, '\n')
    time.sleep(1)

def outside_bets():
    print("Press L to bet on 1-18")
    print("Press E to bet on Even numbers")
    print("Press R to bet on Red")
    print("Press B to bet on Black")
    print("Press O to bet on Odd numbers")
    print("Press U to bet on 19-36")
    print("Press 4 to bet on the 1st column")
    print("Press 5 to bet on the 2nd column")
    print("Press 6 to bet on the 3rd column")
    print("Press 7 to bet on the 1st 12")
    print("Press 8 to bet on the 2nd 12")
    print("Press 9 to bet on the 3rd 12")
    print("Press 0 to exit\n")

def inside_bets():
    print("Press C to make a corner ber")
    print("Press S to make a street bet")
    print("Press T to make a split bet")
    print("Press I to make a line bet")
    print("Press Q to select a number to bet")
    print("Press B to make a basket bet")
    print("Press 0 to exit\n")

def roulette():
    printmenu()
    i = 0
    while True:
        try:
            player_choice = int(input("Please make a bet choice: "))
        except ValueError as e:
            print(e)
            print("Please enter a valid menu option\n")
            continue
        if player_choice not in menu_choices:
            print("Please try again")
        if player_choice in menu_choices:
            break
        i+=1
        if(i > 2):
            print("You have entered too many wrong inputs, goodbye")
            break
    if player_choice == 1:
        while True:
            try:
                bet = int(input("How much would you like to bet? "))
            except ValueError as e:
                print("Invalid input")
                continue
            if bet < 0:
                print("You can't bet less than 0")
                continue
            if bet < table_minimum:
                print("You must bet more than the table minimum")
                continue
            if bet > player_money:
                print("You do not have the funds to make this bet")
                continue
            else:
                break
        player_bet = player_money - bet
        print("You have betted $"+ str(bet) + '\n')
        while True:
            outside_bets()
            answer = input("Your choice: ")
            answer = answer.upper()
            if answer not in choices:
                 print("Not a valid input please try again")
            if answer == "0":
                break
            if answer == "L":
                spin_phrase()
                if result in lower_half:
                    print("You won! $" + str(bet*2))
                    player_bet += bet*2
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "E":
                spin_phrase()
                if result in even:
                    print("You won!")
                    player_bet += bet*2
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "R":
                spin_phrase()
                if result in red:
                    print("You won!")
                    player_bet += bet*2
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "B":
                spin_phrase()
                if result in black:
                    print("You won!")
                    player_bet += bet*2
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "O":
                spin_phrase()
                if result in odd:
                    print("You won!")
                    player_bet += bet*2
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "U":
                spin_phrase()
                if result in upper_half:
                    print("You won!")
                    player_bet += bet*2
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "4":
                spin_phrase()
                if result in first_column:
                    print("You won!")
                    player_bet += bet*3
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "5":
                spin_phrase()
                if result in second_column:
                    print("You won!")
                    player_bet += bet*3
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "6":
                spin_phrase()
                if result in third_column:
                    print("You won!")
                    player_bet += bet*3
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "7":
                spin_phrase()
                if result in first_dozen:
                    print("You won!")
                    player_bet += bet*3
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "8":
                spin_phrase()
                if result in second_dozen:
                    print("You won!")
                    player_bet += bet*3
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            elif answer == "9":
                spin_phrase()
                if result in third_dozen:
                    print("You won!")
                    player_bet += bet*3
                    print("You now have $" + str(player_bet) + '\n')
                else:
                    player_bet = player_bet
                    print("You lost your $" + str(bet) + '\n')
            print("You now have", player_bet)
    if player_choice == 2:
        while True:
            try:
                bet = int(input("How much would you like to bet? "))
            except ValueError as e:
                print("Invalid input")
                continue
            if bet < 0:
                print("You can't bet less than 0")
                continue
            if bet < table_minimum:
                print("You must bet more than the table minimum")
                continue
            if bet > player_money:
                print("You do not have the funds to make this bet")
                continue
            else:
                break
        player_bet = player_money - bet
        print("You have betted $"+ str(bet) + '\n')
        while True:
            inside_bets()
            answer = input("Your choice: ")
            answer = answer.upper()
            if answer not in choices2:
                 print("Not a valid input please try again")
            if answer == "0":
                break
            if answer == "C":
                for index in range(len(corner)):
                    print(index, corner[index])
                answer = int(input("What corner: "))
                spin_phrase()
                if result in corner[answer]:
                    print("you won")
                    print(corner[answer])
                    player_bet += bet*9
                else:
                    print(corner[answer])
                    print("You lost, you have", player_bet)
            if answer == "S":
                for index in range(len(street)):
                    print(index, street[index])
                answer = int(input("What street: "))
                spin_phrase()
                if result in street[answer]:
                    print("you won")
                    print(street[answer])
                    player_bet += bet*12
                else:
                    print("you lost")
            if answer == "T":
                for index in range(len(split)):
                    print(index, split[index])
                answer = int(input("What split: "))
                spin_phrase()
                if result in split[answer]:
                    print("you won")
                    print(split[answer])
                    player_bet += bet*18
                else:
                    print("you lost")
            if answer == "I":
                for index in range(len(line)):
                    print(index, line[index])
                answer = int(input("What line: "))
                spin_phrase()
                if result in line[answer]:
                    print("you won")
                    print(line[answer])
                    player_bet += bet*6
                else:
                    print("you lost")
            if answer == "Q":
                print(straight_up, sep = ", ")
                answer = int(input("what number what you like to bet on? "))
                spin_phrase()
                if answer == result:
                    print("You won, ball landed on", result)
                    player_bet += bet*36
                    print(player_bet)
                else:
                    print("you lost, ball landed on", result)
                    player_bet = player_bet
                    print(player_bet)
    elif player_choice == 0:
        pass
        
roulette()
