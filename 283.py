# make use of 'del' in Python, inspired by:
# https://leetcode.com/discuss/75850/my-simple-and-clear-python-solution-64ms
# Another solution:
# https://discuss.leetcode.com/topic/24844/simple-c-solution-8ms

import sys
from leetcode_util import read_list


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in xrange(len(nums)):
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
            else:
                i += 1

if __name__ == '__main__':
    sol = Solution()
    print sol.moveZeroes(read_list(sys.argv[1]))
