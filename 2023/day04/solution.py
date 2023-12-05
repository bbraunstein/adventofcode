import re
import numpy as np

with open("input.txt", "r") as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall(r"\d+", x))) for x in ls]
wins = [len(set(n[11:]).intersection(set(n[1:11]))) for n in ns]

# Part 1
print(sum(2 ** (w - 1) for w in wins if w > 0))

# Part 2
cards = np.ones(len(ns))
for i in range(len(cards)):
    cards[i + 1 : i + wins[i] + 1] += cards[i]

print(cards.sum())