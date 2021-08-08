# ref: https://leetcode.com/problems/best-sightseeing-pair/discuss/260850/JavaC%2B%2BPython-One-Pass-O(1)-space

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = imax = 0
        # values[i] + values[j] + i - j = values[i] + i + values[j] - j where i < j
        # so we compute them separately
        for i, v in enumerate(values):
            ans = max(ans, imax + v - i)
            # imax is the maximum value of value[i] + i so far
            imax = max(imax, v + i)
        return ans
