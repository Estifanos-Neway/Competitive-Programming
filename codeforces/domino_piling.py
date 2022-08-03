# A. Domino piling
# https://codeforces.com/problemset/problem/50/A
# Easy

def dominoPiling(m, n):
    return (m*n)//2

if __name__ == "__main__":
    m, n = [int(a) for a in input().split(" ")]
    print(dominoPiling(m, n))
