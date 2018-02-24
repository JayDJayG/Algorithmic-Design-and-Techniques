# Uses python3

def calc_fib_mine(n):
    arr = [0, 1]
    if n == 0:
        return 0
    elif n == 1:
        return 1

    else:

        for i in range(2, n + 1):
            arr[0] += arr[1]
            arr[1] += arr[0]


        if n % 2 == 0:
            stringLen= int(len(str(arr[0])))
            return str(arr[0])[stringLen - 1]
        else:
            stringLen= int(len(str(arr[1])))
            return str(arr[1])[stringLen - 1]
                
n = int(input())
print(calc_fib_mine(n))
