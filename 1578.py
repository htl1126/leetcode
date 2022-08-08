# Ref: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/831588/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = max_cost = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                max_cost = 0
            ans += min(max_cost, neededTime[i])  # this line is important
            max_cost = max(max_cost, neededTime[i])
        return ans
