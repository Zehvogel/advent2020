#!/usr/bin/env python3

# SPDX-License-Identifier: MIT


rawdata = []
with open("input") as f:
    rawdata = f.read()

data = rawdata.split("\n\n")

any_count = 0
all_count = 0
for group in data:
    # probably a bit overkill lol
    any_yes = {c for c in group.replace("\n", "")}
    any_count += len(any_yes)
    all_yes = any_yes
    for line in group.split():
        all_yes = all_yes.intersection({c for c in line})
    all_count += len(all_yes)

print(any_count)
print(all_count)
