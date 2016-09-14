class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        if len(nums) < 2:
            return
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        if nums[i] < nums[i + 1]:
            min_idx = i + 1
            for j in xrange(i + 1, len(nums)):
                if nums[j] > nums[i] and nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            nums[i + 1:] = sorted(nums[i + 1:])
        else:
            nums[:] = sorted(nums)
