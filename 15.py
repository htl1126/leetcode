# using list pointers
# fix one element as x, then set y, z to find all solutions for - x = y + z

import sys
from leetcode_util import read_list

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        num = sorted(nums)
        result = []
        for i in xrange(len(num) - 2):
            if i == 0 or num[i - 1] < num[i]:
                negate = - num[i]
                start = i + 1
                end = len(num) - 1
                while start < end:
                    if negate == num[start] + num[end]:
                        result.append([num[i], num[start], num[end]])
                        start += 1
                        end -= 1
                        while start < end and num[start] == num[start - 1]:
                            start += 1
                        while start < end and num[end] == num[end + 1]:
                            end -= 1
                    elif negate < num[start] + num[end]:
                        end -= 1
                    elif negate > num[start] + num[end]:
                        start += 1
        return result

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSum(read_list(sys.argv[1]))
