# Ref: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/117723/Python-standard-DP-solution-with-explanation

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = dp = 0
        pre = -1
        for i in range(len(nums)):
            if nums[i] < left:
                ans += dp
            elif nums[i] > right:
                dp = 0
                pre = i
            else:
                dp = i - pre
                ans += dp
        return ans
