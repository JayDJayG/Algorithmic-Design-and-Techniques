# Uses python3
import sys

def gcd_euclidean(a, b):

    if a > b or a == b:
        big = a
        small = b
    else:
        big = b
        small = a




if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
