# Ref: https://leetcode.com/problems/mirror-reflection/discuss/141773/C%2B%2BJavaPython-1-line-without-using-any-package-or

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p % 2 == 0 and q % 2 == 0:
            p, q = p / 2, q / 2
        return 1 - p % 2 + q % 2

if __name__ == '__main__':
    sol = Solution()
    print sol.mirrorReflection(2, 1)
