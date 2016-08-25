# ref: https://discuss.leetcode.com/topic/30746/share-some-analysis-and
#              -explanations


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + [num for num in nums if num] + [1]
        n = len(nums)
        # dp[i][j]: maximum value for bursting balloons nums[i + 1]...nus[j - 1]
        dp = [[0] * n for _ in xrange(n)]
        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] *
                                          nums[i] * nums[right] +
                                          dp[left][i] + dp[i][right])
        return dp[0][n - 1]

if __name__ == '__main__':
    sol = Solution()
    print sol.maxCoins([3, 8])
