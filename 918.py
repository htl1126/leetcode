# Ref: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, max_sum, cur_max, min_sum, cur_min = 0, nums[0], 0, nums[0], 0
        for n in nums:
            cur_max = max(cur_max + n, n)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + n, n)
            min_sum = min(min_sum, cur_min)
            total += n
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
