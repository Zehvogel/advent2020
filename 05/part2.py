#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import sys

data = sys.stdin.read().split()

last = int(data[-1], 2)

print(last)

for i, seat in enumerate(data):
    if int(seat, 2) + 1 != int(data[i+1], 2):
        print(int(seat, 2) + 1)
        break
