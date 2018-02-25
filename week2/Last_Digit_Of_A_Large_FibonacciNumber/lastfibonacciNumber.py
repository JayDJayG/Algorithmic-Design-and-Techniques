'''
 int first = 0;
    int second = 1;

    int res;

    for (int i = 2; i <= n; i++) {
        res = (first + second) % 10;
        first = second;
        second = res;
    }

    return res;
}
'''




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
        return str(fibList[0])[lenStr -1]

n = int(input())
print(calc_fib_mine(n))
