import sys

# formula solution

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Ref: https://en.wikipedia.org/wiki/Digital_root
        if num:
            return num - 9 * ((num - 1) / 9)
        else:
            return 0
        
if __name__ == '__main__':
    sol = Solution()
    print sol.addDigits(int(sys.argv[1]))
