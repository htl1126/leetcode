# source:
# https://leetcode.com/discuss/46104/simple
#         -java-solution-in-o-n-without-extra-space

import sys
from leetcode_util import read_list


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


if __name__ == '__main__':
    sol = Solution()
    print sol.productExceptSelf(read_list(sys.argv[1]))
