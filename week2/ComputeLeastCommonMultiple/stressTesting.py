#git config --global core.autocrlf true

import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

while True:

    a = random.randint(1, 1000000000)
    b = random.randint(1, 1000000000)

    if lcm(a, b) == lcm_naive(a, b):
        print("Good Job!")
    else:
        print("Wrong")
        print(lcm(a, b), lcm_naive(a, b))


    iterations+= 1
    print(iterations)
