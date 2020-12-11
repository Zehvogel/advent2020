#!/usr/bin/env python3

# SPDX-License-Identifier: MIT

import re


def val_minmax(value, min_v, max_v):
    return value >= min_v and value <= max_v

def val_byr(value):
    return val_minmax(int(value), 1920, 2002)

def val_iyr(value):
    return val_minmax(int(value), 2010, 2020)

def val_eyr(value):
    return val_minmax(int(value), 2020, 2030)

def val_hgt(value):
    if value.endswith("cm"):
        return val_minmax(int(value.rstrip("cm")), 150, 193)
    elif value.endswith("in"):
        return val_minmax(int(value.rstrip("in")), 59, 76)
    else:
        return False

def val_hcl(value):
    if re.fullmatch(r"#[a-f0-9]{6}", value) is not None:
        return True
    else:
        return False

def val_ecl(value):
    accepted = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return value in accepted

def val_pid(value):
    return re.fullmatch(r"[0-9]{9}", value) is not None


rawdata = []
with open("input") as f:
    rawdata = f.read()

data = rawdata.split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

part1_valid = 0
part2_valid = 0

for passport in data:
    kv_data = dict([s.partition(":")[::2] for s in passport.split()])

    valid = True
    for field in required_fields:
        valid &= field in kv_data

    if valid:
        part1_valid += 1
        valid &= val_byr(kv_data["byr"])
        valid &= val_iyr(kv_data["iyr"])
        valid &= val_eyr(kv_data["eyr"])
        valid &= val_hgt(kv_data["hgt"])
        valid &= val_hcl(kv_data["hcl"])
        valid &= val_ecl(kv_data["ecl"])
        valid &= val_pid(kv_data["pid"])

    if valid:
        part2_valid += 1

print(part1_valid)
print(part2_valid)
