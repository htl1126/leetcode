# Ref: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/discuss/877722/Clean-Python-3-O(sort)

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and nums[i] == i else i
