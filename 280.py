# ref: https://leetcode.com/discuss/57113/java-o-n-solution


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(len(nums)):
            if i % 2 == 1:
                if nums[i - 1] > nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            else:
                if i > 0 and nums[i - 1] < nums[i]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]

if __name__ == '__main__':
    sol = Solution()
    print sol.wiggleSort([3, 5, 2, 1, 6, 4])
