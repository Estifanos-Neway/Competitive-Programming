# 1561. Maximum Number of Coins You Can Get
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# Medium

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse=True)
        m = 0
        c = 0
        i = 1
        while c < len(piles)/3:
            m += piles[i]
            c += 1
            i += 2
        return m


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([2,4,1,2,7,8]))
