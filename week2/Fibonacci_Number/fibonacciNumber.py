# Uses python3

'''Design:
Swap algorithm implementation

arr = [] -> Array Target,
#Fi = F(i-1) + F(i-2) -> arr[0] = arr [1] + arr[2]
                        arr[1] = arr[2]
                        arr[2] = arr[0]

'''
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

        return arr[0]


n = int(input())
print(calc_fib_mine(n))
