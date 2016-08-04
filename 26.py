class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last, length = nums[0], 1
        for i in xrange(1, len(nums)):
            if nums[i] != last:
                last = nums[i]
                nums[length] = nums[i]
                length += 1
        nums = nums[:length]
        return len(nums)

if __name__ == '__main__':
    sol = Solution()
    print sol.removeDuplicates([1, 1, 1, 2, 2, 3, 4, 4, 5])
