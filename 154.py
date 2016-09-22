# Really similar to LC 153 with approach in LC 81


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end and nums[end] == nums[end - 1]:
            end -= 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) / 2
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid
        return nums[start]
