# ref: https://discuss.leetcode.com/topic/37710/clean-python-code
# The code is cleaner than Stefan's and idea is good too


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        # ket step: remove trailing numbers same as nums[0]
        while left < right and nums[left] == nums[right]:
            right -= 1
        # then do the same as the problem I
        while left <= right:
            mid = (left + right) / 2
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                num = nums[mid]
            else:
                if target >= nums[0]:
                    num = float('inf')
                else:
                    num = float('-inf')
            if target == num:
                return True
            elif target > num:
                left = mid + 1
            else:
                right = mid - 1
        return False
