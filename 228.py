# concise solution from https://leetcode.com/discuss/63464/7-line-python-implementation

import sys
from leetcode_util import read_list

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        begin = 0
        ans = []
        strout = lambda b, e: '{0}->{1}'.format(b, e) if b != e else str(b)
        for i in xrange(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                ans.append(strout(nums[begin], nums[i - 1]))
                begin = i
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.summaryRanges(read_list(sys.argv[1]))
