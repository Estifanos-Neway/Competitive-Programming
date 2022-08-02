# 1630. Arithmetic Subarrays
# https://leetcode.com/problems/arithmetic-subarrays/
# Medium

class Solution(object):
    def canBeArithmetic(self, nums):
        nums.sort()
        d = nums[1] - nums[0]
        l = nums[1]
        for n in range(2, len(nums)):
            if nums[n] - l == d:
                l = nums[n]
            else:
                return False
        return True

    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        ans = []
        for i in range(len(l)):
            ans.append(self.canBeArithmetic(nums[l[i]:r[i]+1]))
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.checkArithmeticSubarrays(
        [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10]))
