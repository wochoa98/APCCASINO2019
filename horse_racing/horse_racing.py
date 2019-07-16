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

    casino_take = 10

    bets = {}

    @classmethod
    def change_entropy(cls, ent):
        cls.prob_entropy = ent
    
    def __init__(self, horses, temp_low = None, temp_high = None, percip_chance = None, entropy = None):

        entropy = entropy or 0
        temp_low = temp_low or 0
        temp_high = temp_high or 120
        percip_chance = percip_chance or 50

        no_percip_chance = 100 - percip_chance

        self.temp = random.randint(0, 120)
        self.percip = random.choices([0, 1], [no_percip_chance, percip_chance])
        self.horses = horses
        
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

        # subtract bet from player's bankroll

    def payout(self):
        pool = 0

        pool -= pool*self.casion_take

        for horse, player_bet in bets.items():
            for player, bet in player_bet.items():
                pool += bet

        # Subtract casino's take

        winners_pool = 0
        for player, bet in bets[self.winner]:
            winners_pool += bet
        
        for player, bet in bets[self.winner]:
            percent = bet / winners_pool

            player_payout = pool * percent

            # Add player_payout to player's bankroll
