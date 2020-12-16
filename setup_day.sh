#!/bin/bash

if [[ -z "$1" ]]; then
  echo "No day number provided"
  exit
fi

day="day`printf %02d $1`"

if [[ -d $day ]]; then
  echo "$day already exists"
  exit
fi

mkdir $day

touch $day/__init__.py
touch $day/solution.py
touch $day/input.txt
touch $day/test_input.txt

git add $day/*
