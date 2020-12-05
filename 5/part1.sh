#!/usr/bin/env bash

echo $(("2#$(cat input | tr BF 10 | tr RL 10 | sort | tail -n 1)"))
