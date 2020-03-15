# Ref: https://leetcode.com/problems/minimum-area-rectangle-ii/discuss/208351/Python-Complex

import itertools
import collections

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = [complex(*z) for z in sorted(points)]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            seen[P - Q].append((P + Q) / 2)
        ans = float("inf")
        for A, candidates in seen.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                if A.real * (P - Q).real + A.imag * (P - Q).imag == 0:
                    ans = min(ans, abs(A) * abs(P - Q))
        return ans if ans < float("inf") else 0
        
if __name__ == "__main__":
    sol = Solution()
    print sol.minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]])
