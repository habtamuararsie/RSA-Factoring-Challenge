lp = []

"""with open('2T_part1.txt', 'r') as file:
    lines = file.readlines()
    for i in lines:
        for j in list(i.split()):
            lp.append(int(j))
with open("prime.txt", "w") as file:
    for i in lp:
        if i < 15000000:
            file.write(str(i)+",")
"""
from functools import reduce
from math import sqrt

def factors_1(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
print(factors_1(2497885147362973))
