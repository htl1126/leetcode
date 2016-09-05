class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]
        return last + 1

if __name__ == '__main__':
    sol = Solution()
    print sol.removeDuplicates([1, 1, 1, 2, 2, 3, 4, 4, 5])
