# ref: https://discuss.leetcode.com/topic/2048/my-dp-solution-explanation-and
#              -code


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        dp, strlen = [i for i in xrange(len(s))], len(s)
        is_pal = [[False if i != j else True for i in xrange(strlen)]
                  for j in xrange(strlen)]
        for j in xrange(strlen):
            for i in xrange(j + 1):
                if not is_pal[i][j] and s[i:j + 1] == s[i:j + 1][::-1]:
                    is_pal[i][j] = True
                    left, right = i - 1, j + 1
                    while left > 0 and right < strlen and s[left] == s[right]:
                        is_pal[left][right] = True
                        left, right = left - 1, right + 1
                if is_pal[i][j]:
                    dp[j] = 0 if i == 0 else min(dp[i - 1] + 1, dp[j])
        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.minCut('abcccb')
