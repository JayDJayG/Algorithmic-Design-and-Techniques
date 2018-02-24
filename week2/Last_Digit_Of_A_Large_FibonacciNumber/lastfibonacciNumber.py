# Uses python3
def calc_fib_mine(n):
    arr = [0, 1]
    fibList = []
    m =int((n+2)/2)
    counter = 0

    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, m + 2 ) :

            arr[0] += arr[1]
            counter+= 1
            if( counter == n -1):
                fibList.append(arr[0])
                break
            #print(arr[0])

            arr[1] += arr[0]
            counter+=1
            if(counter == n -1):
                fibList.append(arr[1])
                break
            #print(arr[1])

        return fibList[0]

n = int(input())
print(calc_fib_mine(n))
