#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import random


def nop(ip, acc, arg):
    ip += 1
    return ip, acc, arg

def acc(ip, acc, arg):
    acc += arg
    ip += 1
    return ip, acc, arg

def jmp(ip, acc, arg):
    ip += arg
    return ip, acc, arg

def next(ins, arg, ip):
    if ins == "jmp":
        ip += arg
    else:
        ip += 1
    return ip

rawdata = []
with open("input") as f:
    rawdata = f.read()

instructions = {"nop" : nop, "acc" : acc, "jmp" : jmp}

# this split picks up an extra element :(
data = rawdata.split("\n")[:-1]

already_executed = set()

ip = 0
acc = 0
while True:
    if ip in already_executed:
        break
    already_executed.add(ip)
    ins, arg = data[ip].split()
    ip, acc, arg = instructions[ins](ip, acc, int(arg))

print(acc)

coloured = {len(data)}
while True:
    n = len(coloured)
    for i in range(len(data)):
        ins, arg = data[i].split()
        if next(ins, int(arg), i) in coloured:
            coloured.add(i)
            # print("{0} -> {1}".format(i,next(ins, int(arg), i)))
    if n == len(coloured):
        break

for i in already_executed:
    ins, arg = data[i].split()
    if ins == "nop" and int(arg) + i in coloured:
        data[i] = "jmp " + arg
        print("changed data[{0}] to {1}".format(i, data[i]))
        break
    elif ins == "jmp" and i+1 in coloured:
        data[i] = "nop +1"
        print("changed data[{0}] to {1}".format(i, data[i]))
        break
    else:
        continue

ip = 0
acc = 0
while ip < len(data):
    ins, arg = data[ip].split()
    ip, acc, arg = instructions[ins](ip, acc, int(arg))

print(acc)
