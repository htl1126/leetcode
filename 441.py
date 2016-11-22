class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, 2 ** 31 - 1
        while l < r:
            m = (l + r) / 2
            s = m * (m + 1) / 2
            if s > n:
                r = m - 1
            elif s < n:
                l = m + 1
            else:
                return m
        return l if l * (l + 1) / 2 <= n else l - 1

if __name__ == '__main__':
    sol = Solution()
    print sol.arrangeCoins(8)
