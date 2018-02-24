import random

def calc_fib_mine(n):
    arr = [0, 0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:

        for i in range(2, n + 1):
            arr[0] = arr [1] + arr[2]
            arr[1] = arr[2]
            arr[2] = arr[0]

        stringLen= int(len(str(arr[0])))
        return str(arr[0])[stringLen - 1]

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for i in range(n - 1):
        previous, current = current, previous + current

    return current % 10

iterations = 1

while True:

    n = random.randint(0, 10000000)

    if calc_fib_mine(n) == get_fibonacci_last_digit_naive(n):
        print("Good Job!")
    else:
        print("Wrong")
        break

    iterations+= 1
    print(iterations)
