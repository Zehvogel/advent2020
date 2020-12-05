#!/usr/bin/bash

# would be nice to get this in one line :(
NUM="2#"$(cat input | tr BF 10 | tr RL 10 | sort | tail -n 1)
echo $(($NUM))
