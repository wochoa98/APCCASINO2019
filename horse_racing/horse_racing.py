#!/usr/bin/env python

import random
import uuid

class Horse:

    def __init__(self):
        self.id = uuid.uuid4()

        self.speed = random.randint(10,100)
        self.cold_perf = random.randint(1, int(self.speed / 4)) # Cold weather has a small impact on the horses/track
        self.hot_perf = random.randint(1, int(self.speed / 3)) # Heat can have a moderate impact on the horses/track
        self.percip_perf = random.randint(1, int(self.speed / 2)) # Percipitation can have a big impact on the horses/track

class Race:

    prob_entropy = 0

    casino_take = .10

    bets = {}

    @classmethod
    def change_entropy(cls, ent):
        cls.prob_entropy = ent
    
    def __init__(self, entropy = None, horses = None, temp_low = None, temp_high = None, percip_chance = None):

        self.playerList = []

        if entropy == 1:
            entropy = 50
        elif entropy == 2:
            entropy = 300
        elif entropy == 3:
            entropy = 750

        if not horses:
            self.horses = []
            for _ in range(8):
                self.horses.append(Horse())

        entropy = entropy or 1
        temp_low = temp_low or 0
        temp_high = temp_high or 120
        percip_chance = percip_chance or 50

        no_percip_chance = 100 - percip_chance

        self.temp = random.randint(0, 120)
        self.percip = random.choices([0, 1], [no_percip_chance, percip_chance])
        
        self.perf_dict = {}
        self.pre_prob_dict = {}
    
    def calc_pre_odds(self):
        total_sum = 0
        
        for horse in self.horses:
            perf = horse.speed

            if self.percip:
                perf -= horse.percip_perf
            
            if self.temp > 70:
                perf -= horse.hot_perf
            elif self.temp < 35:
                perf -= horse.cold_perf

            self.perf_dict[horse.id] = perf
            total_sum += perf

        print("Pre-race odds:")
        for uid in self.perf_dict:
            self.pre_prob_dict[uid] = round(100 * self.perf_dict[uid] / total_sum)
            print("{}: {}%".format(uid, self.pre_prob_dict[uid]))

        return self.pre_prob_dict
    
    def get_winner(self):
        horses = []
        probs = []
        for horse, prob in self.pre_prob_dict.items():
            horses.append(horse)
            new_prob = prob + random.randint(-1 * self.prob_entropy, self.prob_entropy)
            probs.append(new_prob)
        
        self.winner = random.choices(horses, probs)[0]

        return self.winner

    def place_bet(self, player, horse, ammount):
        bets[horse] = bets[horse] or { }
        bets[horse][player] = ammount

        player.subMoney(ammount)

    def payout(self):
        pool = 0
        
        casino_money = pool*self.casino_take

        self.casinoWinnings += casino_money

        pool -= pool*casino_money

        for horse, player_bet in bets.items():
            for player, bet in player_bet.items():
                pool += bet

        winners_pool = 0
        for player, bet in bets[self.winner]:
            winners_pool += bet
        
        for player, bet in bets[self.winner]:
            percent = bet / winners_pool

            player_payout = pool * percent

            player.addMoney(player_payout)

    def play(self):
        x = self.calc_pre_odds()
        sorted_odds = sorted_x = sorted(x.items(), key=lambda kv: kv[1])
        print(sorted_odds)

        for player in self.playerList:
            if player.playType == 1:
                chosen_horse = sorted_odds[-1][1]
            elif player.playType == 2:
                bet_choice = -1*random.randint(0,2)
                chosen_horse = sorted_odds[bet_choice][1]
            elif player.playType == 3:
                bet_choice = random.randint(0, len(horses))
                chosen_horse = sorted_odds[bet_choice][1]

            # Decide bet ammounts
            bet_ammount = 100
            self.place_bet(player, chosen_horse, bet_ammount)
