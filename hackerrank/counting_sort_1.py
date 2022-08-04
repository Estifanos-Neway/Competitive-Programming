# Counting Sort 1
# https://www.hackerrank.com/challenges/countingsort1/problem
# Easy

def countingSort(arr):
    fa = [0]*100
    for n in arr:
        fa[n] += 1
    return fa

if __name__ == "__main__":
    print(countingSort([2,4,7,67,99,99,2]))