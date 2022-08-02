# 1365. How Many Numbers Are Smaller Than the Current Number
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Easy

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsl = sorted(nums)
        answer = []
        last = 0
        lasti = 0
        for n in nums:
            if n != last:
                last = n
                lasti = numsl.index(n)
            answer.append(lasti)
        return answer
        
if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))