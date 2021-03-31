# ref: https://leetcode.com/problems/russian-doll-envelopes/discuss/1134197/Python-4-lines-solution-explained


class Solution(object):
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [float('inf')] * (len(envelopes) + 1)
        for env in envelopes:
            dp[bisect.bisect_left(dp, env[1])] = env[1]
        return dp.index(float('inf'))

if __name__ == '__main__':
    sol = Solution()
    print sol.maxEnvelopes([[2, 3], [5, 4], [6, 7], [6, 4]])
