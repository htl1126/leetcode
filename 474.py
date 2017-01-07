# ref: https://discuss.leetcode.com/topic/72210/python-7-line-dp-o-kmn-time-o-mn
#              -space-0-1-backpack


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in xrange(m + 1)]
        for dj, dk in [(string.count('0'), string.count('1')) for string in
                       strs]:
            for j in xrange(m, -1, -1):
                for k in xrange(n, -1, -1):
                    if j >= dj and k >= dk:
                        dp[j][k] = max(dp[j][k], dp[j - dj][k - dk] + 1)
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
