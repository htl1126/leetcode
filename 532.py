# Ref: https://leetcode.com/problems/k-diff-pairs-in-an-array/discuss/100135/Easy-Understood-Python-Solution

import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = collections.Counter(nums)
        ans = 0
        for c in cnt:
            if k > 0 and c + k in cnt or k == 0 and cnt[c] > 1:
                ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.findPairs([3, 1, 4, 1, 5], 2)
