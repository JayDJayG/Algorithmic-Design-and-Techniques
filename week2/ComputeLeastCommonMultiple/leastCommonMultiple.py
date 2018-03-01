# Uses python3
import sys

def gcd_euclidean(a, b):

    rest =0

    if a > b or a == b:
        big = a
        small = b
    else:
        big = b
        small = a

    while True:
        rest = big % small
        big = small
        small = rest

        if rest == 0:
            return big

def lcm(a, b):
    div = gcd_euclidean(a, b)
    a = abs(a)
    b = abs(b)

    return (a * b)//div



if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
