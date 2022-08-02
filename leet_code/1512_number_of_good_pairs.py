# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/
# Easy

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    c+=1
        return c
        
if __name__ == "__main__":
    s = Solution()
    print(s.numIdenticalPairs([1,2,3]))