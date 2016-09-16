# ref: https://discuss.leetcode.com/topic/20409/python-o-n-and-o-lgn-solutions
import sys


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return l + (nums[l] < target)
            mid = (l + r) / 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return l  # for [1, 3] target = 0

if __name__ == '__main__':
    sol = Solution()
    nums = [int(num) for num in sys.argv[1].split(',')]
    target = int(sys.argv[2])
    print sol.searchInsert(nums, target)
