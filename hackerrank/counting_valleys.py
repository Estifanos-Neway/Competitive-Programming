# Insertion Sort - Part 1
# https://www.hackerrank.com/challenges/insertionsort1/problem
# Easy

def countingValleys(steps, path):
    m = {"U": 1, "D": -1}
    l = 0
    v = 0
    for p in path:
        if l==-1 and p == "U":
            v+=1
        l += m[p]
    return v


if __name__ == "__main__":
    print(countingValleys(8, "UDDDUDUU"))