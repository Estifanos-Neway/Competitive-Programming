# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Easy

class Stack ():
    def __init__(self):
        self._internalList = []

    def push(self, value):
        self._internalList.append(value)

    def pop(self):
        return self._internalList.pop() if self.length() > 0 else None

    def length(self):
        return len(self._internalList)


class Solution(object):
    tags = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        for t in s:
            if t in self.tags:
                stack.push(t)
            elif not stack.length() or t != self.tags[stack.pop()]:
                return False
        return not stack.length()

if __name__ == "__main__":
    tagsString = ""
    s = Solution()
    print(s.isValid(tagsString))