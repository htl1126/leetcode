# one-linear solution:
# https://leetcode.com/discuss/76003/python-one-liner-100%25-of-solutions-beat-a-little-odd

import sys

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return "{:b}".format(int(a, 2)+int(b, 2))
        
if __name__ == '__main__':
    sol = Solution()
    print sol.addBinary(sys.argv[1], sys.argv[2])
