# Ref: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained
# Algo: dynamic programming

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            ans = 0
            for k in xrange(max(0, target - f), target):
                ans += dp(d - 1, k)
            memo[(d, target)] = ans
            return ans
        return dp(d, target) % (10 ** 9 + 7)

if __name__ == "__main__":
    sol = Solution()
    print sol.numRollsToTarget(2, 6, 7)
