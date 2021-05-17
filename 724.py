class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l, r, i, size = 0, sum(nums[1:]), 0, len(nums)
        while i < size:
            if l == r:
                return i
            if i == size - 1:
                break
            l, r = l + nums[i], r - nums[i + 1]
            i += 1
        return -1
