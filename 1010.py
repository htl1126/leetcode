# Ref: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        c = [0 for _ in xrange(60)]
        ans = 0
        for t in time:
            ans += c[-t % 60]
            c[t % 60] += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.numPairsDivisibleBy60([60, 60, 60])
