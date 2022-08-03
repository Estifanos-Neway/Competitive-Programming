# Insertion Sort - Part 1
# https://www.hackerrank.com/challenges/insertionsort1/problem
# Easy
    
def insertionSort1(n, arr):
    l = arr[-1]
    for i in range(len(arr)):
        if i+1 == n:
            arr[0] = l
            print(" ".join([str(n) for n in arr]))
            return
        c = arr[-(i+2)]
        if c > l:
            arr[-(i+1)] = c
            print(" ".join([str(n) for n in arr]))
        else:
            arr[-(i+1)] = l
            print(" ".join([str(n) for n in arr]))
            return


if __name__ == "__main__":
    insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
