# Ref: https://leetcode.com/problems/partition-array-according-to-given-pivot/discuss/1747184/JavaPython-3-2-methods-w-brief-explanation-and-analysis.

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i = l = 0
        j = r = len(nums) - 1
        ans = [0] * len(nums)
        while i < len(nums):
            if nums[i] < pivot:
                ans[l] = nums[i]
                l += 1
            if nums[j] > pivot:
                ans[r] = nums[j]
                r -= 1
            i, j = i + 1, j - 1
        while l <= r:
            ans[l] = pivot
            l += 1
        return ans
