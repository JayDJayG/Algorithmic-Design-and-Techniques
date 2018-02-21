#git config --global core.autocrlf true

from fibonacci import calc_fib
from fibonacciNumber import calc_fib_mine
import random

iterations = 1

while True:

    n = random.randint(0, 40)

    if calc_fib(n) == calc_fib_mine(n):
        print("Good Job!")
    else:
        print("Wrong")
        break

    iterations+= 1
    print(iterations)
