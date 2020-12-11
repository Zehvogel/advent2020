#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import re

rawdata = []
with open("input") as f:
    rawdata = f.read()

pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

matches = pattern.finditer(rawdata)

part1_valid = 0
part2_valid = 0

for match in matches:
    param1 = int(match.group(1))
    param2 = int(match.group(2))
    char = match.group(3)
    password = match.group(4)
    count = password.count(char)
    if (count >= param1 and count <= param2):
        part1_valid += 1
    if (bool(password[param1 - 1] == char) ^ bool(password[param2 - 1] == char)):
        part2_valid += 1

print(part1_valid)
print(part2_valid)
