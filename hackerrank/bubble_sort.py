# Sorting: Bubble Sort
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
# Easy

def countSwaps(nums):
    s = 0
    n = len(nums)
    for i in range(n):
        for j in range(n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                s += 1
    print("Array is sorted in "+str(s)+" swaps.")
    print("First Element: "+str(nums[0]))
    print("Last Element: "+str(nums[-1]))


if __name__ == '__main__':
    countSwaps([5, 2, 3])
