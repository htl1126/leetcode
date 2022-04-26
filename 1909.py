# Ref: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1298517/Python%3A-Explained%3A-Easy-to-understand%3A-O(n)-Time-and-O(1)-Space

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        idx, count = -1, 0
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                idx, count = i, count + 1

        if count == 0:
            return True

        if count == 1:
            if idx == 0 or idx == len(nums) - 2:
                return True
            if nums[idx - 1] < nums[idx + 1] or idx + 2 < len(nums) and nums[idx] < nums[idx + 2]:
                return True

        return False
