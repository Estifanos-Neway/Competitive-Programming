# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Medium

import math

class Solution(object):
    def getDist(self, point):
        return math.sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=self.getDist)
        return points[:k]

if __name__ == "__main__":
    s = Solution()
    print(s.kClosest([[1,3],[-2,2]], 1))
