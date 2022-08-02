# 1985. Find the Kth Largest Integer in the Array
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
# Medium

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums.sort(key=int)
        return nums[-k]
        
if __name__ == "__main__":
    s = Solution()
    print(s.kthLargestNumber(["3","6","7","10"],4))