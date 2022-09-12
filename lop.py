#!/usr/bin/python3
lp = []
with open("prime.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
        lp.append(int(line))
