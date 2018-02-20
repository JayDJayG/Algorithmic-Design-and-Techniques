#git config --global core.autocrlf true

result = 0

arr = []
n = len(arr)

def mpp(arr):
    arrSorted = sorted(arr)
    return (arrSorted[n - 1] * arrSorted[n - 2])


def max_pairwise_product(arr, n)
    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result
