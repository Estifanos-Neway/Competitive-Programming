# 2089. Find Target Indices After Sorting Array
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
# Easy

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        nums.sort()
        ans = []
        try:
            i = nums.index(target)
        except:
            return []
        while i < l and nums[i] == target:
            ans.append(i)
            i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.targetIndices([1, 2, 5, 2, 3], 5))
