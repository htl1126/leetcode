class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = more = 0
        for n in nums:
            if n < target:
                less += 1
            elif n > target:
                more += 1
        return range(less, len(nums) - more)
