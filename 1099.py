# Ref: https://leetcode.com/problems/two-sum-less-than-k/discuss/331770/Simple-python-solution

import collections

class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        for idx, val in enumerate(A):
            d[val] = idx
        for k in xrange(K - 1, min(A), -1):
            for i in xrange(len(A)):
                if k - A[i] in d and d[k - A[i]] != i:
                    return k
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60)
