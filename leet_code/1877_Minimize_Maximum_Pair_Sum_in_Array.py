# 1877. Minimize Maximum Pair Sum in Array
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Medium

class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m = nums[0] + nums[-1]
        for i in range(1,len(nums)//2):
            s = nums[i] + nums[-i-1]
            if s > m:
                m = s
        return m
            

if __name__ == "__main__":
    s = Solution()
    print(s.minPairSum([2,4,1,2,7,8]))
