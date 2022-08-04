# A. Theatre Square
# https://codeforces.com/problemset/problem/1/A
# Easy

import math
 
def theatreSquare(m, n, a):
    return math.ceil(m/a)*math.ceil(n/a)
 
if __name__ == "__main__":
    m, n, a = [int(n) for n in input().split(" ")]
    print(theatreSquare(m, n, a))