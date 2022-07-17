# Ref: https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/discuss/2292193/Python3-O(n).-Find-min-and-max-value-index

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minidx, maxidx = -1, -1
        for i, v in enumerate(nums):
            if minidx < 0 or nums[i] < nums[minidx]:
                minidx = i
            if maxidx < 0 or nums[i] >= nums[maxidx]:
                maxidx = i
        return minidx + (len(nums) - 1 - maxidx) - (minidx > maxidx)
