#!/usr/bin/env python

from horse_racing import Horse
from horse_racing import Race
import sys

horses = []
for _ in range(8):
    horses.append(Horse())


# Temp low, temp high, percent percipitation
race1 = Race(horses)

race1.play()

