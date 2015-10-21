import sys

# math solution

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print sol.canWinNim(int(sys.argv[1]))
