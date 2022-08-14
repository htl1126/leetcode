class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = max(nums[:2]), min(nums[:2])
        for i in range(2, len(nums)):
            if first < nums[i]:
                first, second = nums[i], first
            elif second < nums[i]:
                second = nums[i]
        return (first - 1) * (second - 1)
