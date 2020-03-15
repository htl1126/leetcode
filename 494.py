# Ref: https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood

import collections

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        count = collections.Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]

if __name__ == "__main__":
    sol = Solution()
    print sol.findTargetSumWays([1, 1, 1, 1, 1], 3)
