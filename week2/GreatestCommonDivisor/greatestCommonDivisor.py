# Uses python3
import sys

'''
Divide 210 by 45, and get the result 4 with remainder 30, so 210=4·45+30.
Divide 45 by 30, and get the result 1 with remainder 15, so 45=1·30+15.
Divide 30 by 15, and get the result 2 with remainder 0, so 30=2·15+0.
The greatest common divisor of 210 and 45 is 15.
'''
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
