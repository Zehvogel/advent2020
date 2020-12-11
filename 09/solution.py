#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

from collections import deque

input_file = "input"
N = 5 if input_file == "test_input" else 25
rawdata = []
with open(input_file) as f:
    rawdata = f.read()

data = [int(n) for n in rawdata.strip().split()]

numbers = deque(data[:N])

def invalid(d):
    for n in numbers:
        if d-n in numbers and not d-n == n:
            return False
    return True

dataa = data[N:]
the_number = 0
for d in dataa:
    if invalid(int(d)):
        print(d)
        the_number = d
        break
    numbers.popleft()
    numbers.append(d)

res = 0
# probably not the most efficient way
for i in range(2,len(data)):
    for j in range(len(data)-i):
        num = 0
        for k in range(i):
            num += data[j+k]
        if num == the_number:
            seq = data[j:j+i-1]
            res = min(seq) + max(seq)
            break
    if res > 0:
        break
print(res)


