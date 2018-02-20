#Uses python3
n = int(input())
a = [int(x) for x in input().split()]

arr = sorted(a)
print(arr[n - 1] * arr[n - 2])
