#!/usr/bin/env python

from horse_racing import Horse
from horse_racing import Race
import sys

horses = []
for _ in range(8):
    horses.append(Horse())

race1 = Race(horses)

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


winners = {}

Race.change_entropy(int(sys.argv[1]))

for _ in range(1000):
    winner = race1.get_winner()

    if winner in winners:
        winners[winner] += 1
    else:
        winners[winner] = 1
print("*****")
for w, count in winners.items():
    print("{}: {}".format(w, count))
