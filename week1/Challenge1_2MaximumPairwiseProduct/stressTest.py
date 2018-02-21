#git config --global core.autocrlf true
import random

iterations = 1

#My implementation: Faster and simplier 
def mpp(arr):
    arrSorted = sorted(arr)
    arrLen = len(arrSorted)
    return (arrSorted[arrLen - 1] * arrSorted[arrLen - 2])


#Slow implementation gave by the course to make Stressingtest
def max_pairwise_product(arr):
    result = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            if arr[i]*arr[j] > result:
                result = arr[i]*arr[j]

    return result



#Infinite loop to review if both algorithm implementation give the same output
while True:
    n = random.randint(2, 1000)
    arr=[]


    for i in range(random.randint(2, n)):
        arr.append(random.randint(0, 200000))

    if mpp(arr) == max_pairwise_product(arr):
        print("Good Job!")
    else:
        print("Wrong")
        break

    iterations+=1
    print(iterations)
