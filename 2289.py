# Ref: https://leetcode.com/problems/steps-to-make-array-non-decreasing/discuss/2085864/JavaC%2B%2BPython-Stack-%2B-DP-%2B-Explanation-%2B-Poem

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack[-1]])
                stack.pop()
            stack.append(i)
        return max(dp)
