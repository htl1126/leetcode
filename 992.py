# Ref: https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window

import collections

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        ans = i = 0
        for j in xrange(len(A)):
            if count[A[j]] == 0:
                K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    K += 1
                i += 1
            ans += j - i + 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
