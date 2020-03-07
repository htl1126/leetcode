# Ref: https://leetcode.com/problems/dice-roll-simulation/discuss/404840/Short-Python-DP-with-detailed-image-explanation
# Algo: dynamic programming

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        faces = len(rollMax)
        dp = [[0 for _ in xrange(faces + 1)] for _ in xrange(n + 1)]

        dp[0][faces] = 1
        for i in xrange(faces):
            dp[1][i] = 1
        dp[1][faces] = 6

        for i in xrange(2, n + 1):
             for j in xrange(faces):
                  for k in xrange(1, rollMax[j] + 1):
                      if i - k < 0:
                          break
                      dp[i][j] += dp[i - k][faces] - dp[i - k][j]
             dp[i][faces] = sum(dp[i])

        return dp[n][faces] % (10 ** 9 + 7)

if __name__ == "__main__":
    sol = Solution()
    print sol.dieSimulator(3, [1, 1, 1, 2, 2, 3])
