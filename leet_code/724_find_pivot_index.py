# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
# Easy

class Solution(object):
    def pivotIndex(self, nums):
        preSum = [0]
        preSumReverse = [0]
        
        for i in range(len(nums)):
            preSum.append(preSum[-1] + nums[i])
            preSumReverse.insert(0, preSumReverse[0]+nums[-(i+1)])
        preSum.append(0)
        preSumReverse.insert(0, 0)
        for pi in range(len(nums)):
            if (preSum[pi] == preSumReverse[pi+2]):
                return pi
        return -1
    
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    s = Solution()
    print(s.pivotIndex(nums))