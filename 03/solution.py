#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

def positions(data, down, right):
    for i in range(len(data)//down):
        yield data[i*down][i*right % len(data[0])]


def count_trees(data, down, right):
    trees = 0
    for pos in positions(data, down, right):
        if pos == "#":
            trees += 1
    return trees


rawdata = []
with open("input") as f:
    rawdata = f.read()

data = rawdata.split()

part1 = count_trees(data, 1, 3)

print(part1)

part2 = count_trees(data, 1, 1)
part2 *= count_trees(data, 1, 3)
part2 *= count_trees(data, 1, 5)
part2 *= count_trees(data, 1, 7)
part2 *= count_trees(data, 2, 1)

print(part2)
