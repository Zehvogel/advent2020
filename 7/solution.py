#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import re


def n_bags_in_bag(bags, bag):
    n = 0
    for b in iter(bags[bag]):
        n += int(bags[bag][b]) * (1 + n_bags_in_bag(bags, b))
    return n


rawdata = []
with open("input") as f:
    rawdata = f.read()

line_pattern = re.compile(r"(\w+ \w+) bags contain (.+).")

line_matches = line_pattern.finditer(rawdata)

content_pattern = re.compile(r"(\d) (\w+ \w+)")

bags = {}

for match in line_matches:
    content_matches = content_pattern.finditer(match.group(2))
    bags[match.group(1)] = {x.group(2): x.group(1) for x in content_matches}

candidates = {"shiny gold"}

old_length = 0
new_length = len(candidates)

while new_length > old_length:
    for k in iter(bags):
        if any(c in bags[k] for c in candidates):
            candidates.add(k)

    old_length = new_length
    new_length = len(candidates)

# need to subtract the shiny gold bag
print(len(candidates)-1)

print(n_bags_in_bag(bags, "shiny gold"))
