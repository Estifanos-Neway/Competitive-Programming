# Selection Sort
# https://practice.geeksforgeeks.org/problems/selection-sort/1
# Easy

class Solution:
    def select(self, arr, i):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                i = j
        return i

    def selectionSort(self, arr, n):
        for i in range(n):
            j = self.select(arr, i)
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    nums = [6,2,4,8,3,9,22,6,0,3,6]
    s = Solution()
    s.selectionSort(nums,len(nums))
    print(nums)
