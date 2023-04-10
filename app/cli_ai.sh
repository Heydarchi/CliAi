#!/bin/bash

# Read input from stdin and pass it to CliAi
input=$(cat -)
echo "$input" | python CliAi.py run --input -
