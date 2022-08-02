# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/
# Medium

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for c in range(len(nums)):
            num = nums[i]
            if num == 0:
                del nums[i]
                nums.insert(0, 0)
                i += 1
            elif num == 2:
                del nums[i]
                nums.append(2)
            else:
                i += 1


if __name__ == "__main__":
    colors = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(colors)
    print(colors)
