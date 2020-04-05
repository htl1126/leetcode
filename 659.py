# Ref: https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/Python-Easy-Understand-Greedy
# Algo: greedy

import collections

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            if not left[i]:
                continue
            left[i] -= 1
            if end[i - 1]:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isPossible([1, 2, 3, 3, 4, 4, 5, 5])
