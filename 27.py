class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_len = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[new_len] = nums[i]
                new_len += 1
        return new_len
