class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        l, r = 0, s
        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1
