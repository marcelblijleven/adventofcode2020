#!/bin/bash

if [[ -z "$1" ]]; then
  echo "No day number provided"
  exit
fi

day="day$(printf %02d "$1")"

if [[ -d $day ]]; then
  echo "$day already exists"
  exit
fi

mkdir "$day"

touch "$day/__init__.py"
touch "$day/input.txt"
touch "$day/test_input.txt"

{
  printf "from util import get_input\n\n"
  printf "TEST_INPUT = get_input('test_input.txt')\n"
  printf "INPUT = get_input('input.txt')\n\n\n"
  printf "def part_one(_input):\n\tpass\n\n\n"
  printf "def part_two(_input):\n\tpass\n\n"
} >> "$day/solution.py"

git add "$day/*"
