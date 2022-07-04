class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]  # median
        return sum(abs(n - m) for n in nums)
