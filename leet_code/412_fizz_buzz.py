# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# Easy

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzBuzzList = []
        for i in range(n+1):
            if i % 15 == 0:
                fizzBuzzList.append("FizzBuzz")
            elif i % 5 == 0:
                fizzBuzzList.append("Buzz")
            elif i % 3 == 0:
                fizzBuzzList.append("Fizz")
            else:
                fizzBuzzList.append(str(i))
        del fizzBuzzList[0]
        return fizzBuzzList
if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(30))