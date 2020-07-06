# Ref: https://leetcode.com/problems/hamming-distance/discuss/94789/Beats-100-Python

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = x ^ y
        ans = 0
        while s:
            ans += 1
            s &= (s - 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.hammingDistance(1, 4)
