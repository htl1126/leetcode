# magic one-liner: https://leetcode.com/discuss/67164/one-line-solution-in-python

import sys
from leetcode_util import read_list

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

if __name__ == '__main__':
    sol = Solution()
    print sol.containsDuplicate(read_list(sys.argv[1]))
