class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        min_diff, ans = float('inf'), 0
        for i, v in enumerate(nums):
            left, right = left + v, right - v
            if i + 1 < len(nums):
                diff = abs(left // (i + 1) - right // (len(nums) - 1 - i))
            else:
                diff = left // (i + 1)
            if diff < min_diff:
                min_diff, ans = diff, i
        return ans
