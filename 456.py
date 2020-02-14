# Ref: https://leetcode.com/problems/132-pattern/discuss/94081/10-line-Python-Solution

import sys

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # reverse the sequence and find the '231' pattern
        stack = []
        s3 = -sys.maxint
        for n in nums[::-1]:
            if n < s3:
                return True # found the '1' pattern
            while stack and stack[-1] < n: # found the '23' pattern
                s3 = stack.pop()
            stack.append(n)
        return False
        
if __name__ == "__main__":
    sol = Solution()
    print find132pattern([3, 1, 4, 2])
