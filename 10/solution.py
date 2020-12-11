#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import numpy as np

input_file = "input"
rawdata = []
with open(input_file) as f:
    rawdata = f.read()

data = np.insert(np.asarray(rawdata.split(), dtype=np.int), 0, 0)
data.sort()
data = np.append(data, data[-1]+3)

differences = data[1:] - data[:-1]

ones = np.count_nonzero(differences == 1)
threes = np.count_nonzero(differences == 3)
print(ones * threes)

def can_reach(i):
    res = []
    for j in range(1,4):
        if i-j < 0:
            break
        elif data[i] - data[i-j] <= 3:
            res.append(i-j)
        else:
            break
    return res

acombs = [1, 1]
for i in range(2, len(data)):
    combs = 0
    for j in can_reach(i):
        combs += acombs[j]
    acombs.append(combs)

print(acombs[-1])
