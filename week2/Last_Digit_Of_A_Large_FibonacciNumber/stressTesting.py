import random

def calc_fib_mine(n):
    arr = [0, 1]
    fibList = []
    m =int((n+2)/2)
    counter = 0

    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, m + 2 ) :

            arr[0] += arr[1] % 10
            counter+= 1
            if( counter == n -1):
                fibList.append(arr[0])
                break

            arr[1] += arr[0] %10
            counter+=1
            if(counter == n -1):
                fibList.append(arr[1])
                break

        lenStr = len(str(fibList[0]))
        return int(str(fibList[0])[lenStr -1])

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

    n = random.randint(0, 1000000)

    if calc_fib_mine(n) == get_fibonacci_last_digit_naive(n):
        print("Good Job!")
    else:
        print("Wrong")
        print(calc_fib_mine(n), get_fibonacci_last_digit_naive(n))


    iterations+= 1
    print(iterations)
