# Ref: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque

import collections

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    print sol.shortestSubarray([2, -1, 2], 3)
