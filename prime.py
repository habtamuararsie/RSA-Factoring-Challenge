#!/usr/bin/python3
lp = []
with open("prime.txt", 'r') as file:
        for line in file:
            lp=line[:-1].split(",")
            break

from functools import reduce
from math import sqrt
def factors_1(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


"""def isprime(n):
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    divs = range(5, int(n ** 0.5) + 1, 2)
    return [d for d in itertools.chain(divs[::3], divs[1::3]) if n % d == 0][0]
"""
def factor(n):
    for i in lp:
        j = int(i)
        if n % j == 0:
            if j == n:
                return 1
            return j
    #lpi = [i for i in range (100001, int(n ** .5)+1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
    """for i in range (100000001, int(n ** .5)+1,2):
        if n % i == 0:
            return i
    divs = range(1000003, int(n ** 0.5) + 1, 2)
    l = [d for d in itertools.chain(divs[::3], divs[1::3]) if n % d == 0]
    if l != []:
        return l[0]
    k = 166660
    while 6*k+1 <= int(n**0.5) + 1:
        if n % (6*k+1) == 0:
            return 6*k+1
        if n % (6*k-1) == 0:
            return 6*k-1"""

    if n > 15000000:
        li=[(6*i+1, 6*i-1) for i in range(2499999, int((int(n**.5) + 1)/6) + 1) if (n % (6*i+1) == 0 or n % (6*i-1) == 0)]
        if li != []:
            for i in li[0]:
                if n % i == 0:
                    return i

        """for i in range(1666660, int((int(n**.5) + 1)/6) + 1):
            if n % (6*i+1) == 0:
                print("ijoij")
                return 6*i+1
            if n % (6*i-1) == 0:
                return 6*i-1
        li=[(6*i+1, 6*i-1) for i in range(1666660, int((int(n**.5) + 1)/6) + 1) if (n % (6*i+1) == 0, n % (6*i-1) == 0)]"""
    return 1
def primef(n):
    if n <= 3:
        return int(n)
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    else:
        for i in range(5, int((n)**0.5) + 1, 6):
            if n % i == 0:
                return int(i)
            if n % (i + 2) == 0:
                return primef(n/(i+2))
    return int(n)
