#!/usr/bin/env python

from horse_racing import Horse
from horse_racing import Race
import sys

horses = []
for _ in range(8):
    horses.append(Horse())

try:
    sys.argv[3]
except IndexError:
    print("Need 3 arguments:")
    print("test_conditions.py <min temperature> <max temperature> <percent chance of perciptiation>")
    quit()


# Temp low, temp high, percent percipitation
race1 = Race(horses, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

race1.calc_pre_odds()

winners = {}


for _ in range(1000):
    winner = race1.get_winner()

    if winner in winners:
        winners[winner] += 1
    else:
        winners[winner] = 1
print("*****")
for w, count in winners.items():
    print("{}: {}".format(w, count))
    
