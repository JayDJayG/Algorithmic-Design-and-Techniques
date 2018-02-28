import random
import sys

iterations = 1

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


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


while True:

    a = random.randint(1, 1000000000)
    b = random.randint(1, 1000000000)

    if gcd_euclidean(a, b) == gcd_naive(a, b):
        print("Good Job!")
    else:
        print("Wrong")
        print(gcd_euclidean(a, b), gcd_naive(a, b))


    iterations+= 1
    print(iterations)
