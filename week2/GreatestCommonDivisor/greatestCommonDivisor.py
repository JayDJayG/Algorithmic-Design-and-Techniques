# Uses python3
import sys

def gcd_euclidean(a, b):

    if a > b or a == b:
        big = a
        small = b
    else:
        big = b
        small = a

    rest =0
    total = 0


    while True:
        rest = big % small
        big = small
        small = rest

        if rest == 0:
            return big


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))
