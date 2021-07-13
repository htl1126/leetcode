# ref: https://discuss.leetcode.com/topic/37710/clean-python-code
# The code is cleaner than Stefan's and idea is good too


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        # this loop avoids case [1, 0, 1, 1, 1], target = 0
        while left < right and nums[left] == nums[right]:  # check "left < right" for case [1]
            right -= 1
        while left <= right:
            mid = (left + right) // 2
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
