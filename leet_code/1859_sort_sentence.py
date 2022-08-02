# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/
# Easy

class Solution(object):
    def getIndex(self,w):
        return w[-1]
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """

        wl = s.split()
        wl.sort(key=self.getIndex)
        return " ".join([w[0:-1] for w in wl])
if __name__ == "__main__":
    s = Solution()
    print(s.sortSentence("sentence4 a3 is2 This1"))