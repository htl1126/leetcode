class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        ans = 0
        while z:
            ans += z & 1
            z >>= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.hammingDistance(1, 4)
