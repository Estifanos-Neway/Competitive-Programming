# 946. Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/
# Medium

class Solution(object):
    def validateStackSequences(self, pushed:list, popped:list):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        pushedPointer = 0
        
        while len(pushed) > 0:
            poppedValue = popped[0]
            try:
                i = pushed.index(poppedValue)
                if(i<pushedPointer):
                    return False
                pushedPointer = i-1
                pushed.remove(poppedValue)
                popped.remove(poppedValue)
            except:
                return False
        return True

if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    s = Solution()
    print(s.validateStackSequences(pushed, popped))