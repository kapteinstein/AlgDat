from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict

def l():
    d = int(stdin.readline())
    strings = []
    maximum = 0
    for line in stdin:
        strings.append(line.rstrip())
        if len(strings[-1]) > maximum:
            maximum = len(strings[-1])
    print(maximum)
l()

