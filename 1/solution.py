#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import numpy as np

def part1(data):
    for i in range(data.size):
        for j in range(i+1, data.size):
            tmp = data[i] + data[j]
            if tmp == 2020:
                return data[i] * data[j]

def part2(data):
    for i in range(data.size):
        for j in range(i+1, data.size):
            for k in range(j+1, data.size):
                tmp = data[i] + data[j] + data[k]
                if tmp == 2020:
                    return data[i] * data[j] * data[k]

rawdata = []
with open("input") as f:
    rawdata = f.read()

data = np.asarray(rawdata.split(), dtype=np.uint)

print(part1(data))
print(part2(data))
