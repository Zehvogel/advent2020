#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import copy


def pretty_print(data):
    for d in data:
        print("".join(d))
    print()


input_file = "input"
rawdata = []
with open(input_file) as f:
    rawdata = f.read()

data = [list(s) for s in rawdata.strip().split()]
max_x = len(data[0]) - 1
max_y = len(data) - 1
new_data = copy.deepcopy(data)

def update_part_one(x, y):
    x_l = x - 1 if x - 1 >= 0 else 0
    x_h = x + 1 if x + 1 <= max_x else max_x
    y_l = y - 1 if y - 1 >= 0 else 0
    y_h = y + 1 if y + 1 <= max_y else max_y

    occupied = 0
  #  print(list(range(y_l, y_h + 1)), list(range(x_l, x_h +1)))
    for _y in range(y_l, y_h + 1):
        for _x in range(x_l, x_h + 1):
            if _x == x and _y == y:
                continue
            if data[_y][_x] == "#":
    #            print(_y, _x, data[_y][_x])
                occupied += 1

   # print(y, x, data[y][x], occupied)

    if data[y][x] == "L" and occupied == 0:
        new_data[y][x] = "#"
        return True
    elif data[y][x] == "#" and occupied >= 4:
        new_data[y][x] = "L"
        return True
    else:
        return False

def update_part_two(x, y):
    occupied = 0
    i_x = [-1, 0, 1]
    i_y = [-1, 0, 1]

    for i in i_x:
        for j in i_y:
            if i == 0 and j == 0:
                continue
            k = 1
            x_i = x+k*i
            y_j = y+k*j
            while x_i >= 0 and x_i <= max_x and y_j >= 0 and y_j <= max_y:
                seat = data[y_j][x_i]
                if seat == ".":
                    k += 1
                    x_i = x+k*i
                    y_j = y+k*j
                    continue
                elif seat == "#":
                    occupied += 1
                break
    if data[y][x] == "L" and occupied == 0:
        new_data[y][x] = "#"
        return True
    elif data[y][x] == "#" and occupied >= 5:
        new_data[y][x] = "L"
        return True
    else:
        return False

changed = True

#pretty_print(data)
while changed:
    changed = False
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if data[y][x] == ".":
                continue
            else:
                changed |= update_part_two(x, y)
    data = copy.deepcopy(new_data)
    #pretty_print(data)

n_occupied = 0
for d in data:
    n_occupied += d.count("#")

print(n_occupied)

