#!/usr/bin/bash

cat input | tr BF 10 | tr RL 10 | sort | python part2.py
