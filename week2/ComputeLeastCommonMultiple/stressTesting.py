#git config --global core.autocrlf true

import sys
import random

def gcd_euclidean(a, b):

    if a > b or a == b:
        big = a
        small = b
    else:
        big = b
        small = a

    rest =0
    total = 0


    while True:
        rest = big % small
        big = small
        small = rest

        if rest == 0:
            return big

def lcm(a, b):

    return ((a*b)/gcd_euclidean(a, b))


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

iterations =0
while True:

    a = random.randint(1, 10000)
    b = random.randint(1, 1000)

    if lcm(a, b) == lcm_naive(a, b):
        print("Good Job!")
    else:
        print("Wrong")
        print(lcm(a, b), lcm_naive(a, b))


    iterations+= 1
    print(iterations)
