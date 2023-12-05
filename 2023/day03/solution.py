import itertools
import re
import math

with open("input.txt", "r") as f:
    ls = f.read().strip().split("\n")

# Cartesian product, i.e quick and easy way to plot a 3x3 box
box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))

# Iterate over elements in `ls` using a nested `for` loop
# and identify all instances of a symbo using dict comprehension
# Create a key-value dict where:
#   the key is a tuple representing the (row, line_index) coordinate of a symbol and
#   the value is a another tuple, (char, []), containing the matched symbol and an empty list
parts_by_symbol = {
    (row, line_index): (char, [])
    for row, col in enumerate(ls)
    for line_index, char in enumerate(col)
    if char != "." and not char.isdigit()
}

# print(parts_by_symbol.keys())
part_sum = 0

for row, col in enumerate(ls):
    for match in re.finditer(r"\d+", col):
        n = int(match.group(0))
        # For every matched digit, plot a box of coordinates around it
        boundary = {
            (row + di, j + dj)
            for di, dj in box
            for j in range(match.start(), match.end())
        }
        # Bitwise comparison to find if symbol coordinates exists
        # within boundary coordinates
        if parts_by_symbol.keys() & boundary:
            # print(parts_by_symbol.keys() & boundary)
            part_sum += n
        # For part 2: append the 2nd tuple with the matched number(s)
        for symbol in parts_by_symbol.keys() & boundary:
            parts_by_symbol[symbol][1].append(n)
            print(parts_by_symbol[symbol])

# part 1
print(part_sum)

# part 2
# Calculate sum of product for matched parts, where the length
# of the parts tuple is equal to 2 and the part symbol is an asterisk '*'
print(
    sum(
        math.prod(parts)
        for symbol, parts in parts_by_symbol.values()
        if len(parts) == 2 and symbol == "*"
    )
)
