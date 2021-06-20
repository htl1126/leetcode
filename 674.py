class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start, ans = 0, 1
        for k in range(1, len(nums)):
            if nums[k] > nums[k - 1]:
                ans = max(ans, k - start + 1)
            else:
                start = k
        return ans
