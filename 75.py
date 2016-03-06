# source: https://leetcode.com/discuss/84177/python-o-n-1-pass
#                 -in-place-solution-with-explanation

import sys
from leetcode_util import read_list


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        second = len(nums) - 1
        i = 0
        while i <= second:
            while nums[i] == 2 and i < second:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1
        return nums


if __name__ == '__main__':
    sol = Solution()
    print sol.sortColors(read_list(sys.argv[1]))
