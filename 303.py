# too slow, need to be speed up

import sys
from leetcode_util import read_list

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.table = nums
        for i in xrange(1, len(self.table)):
            self.table[i] += self.table[i - 1]
        self.table = [0] + self.table

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.table[j + 1] - self.table[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

if __name__ == '__main__':
    numArray = NumArray(read_list(sys.argv[1]))
    print numArray.sumRange(0, 4)
    print numArray.sumRange(1, 3)
