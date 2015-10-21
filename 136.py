import sys
from leetcode_util import read_list

# Use XOR magic https://leetcode.com/discuss/62111/
#                       one-line-python-solution-with-o-n-time

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == '__main__':
    sol = Solution()
    print sol.addDigits(read_list(sys.argv[1]))
