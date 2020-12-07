#!/usr/bin/bash

# SPDX-License-Identifier: MIT

cat input | tr BF 10 | tr RL 10 | sort | python part2.py
