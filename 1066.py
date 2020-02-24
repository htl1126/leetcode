# Ref: https://leetcode.com/problems/campus-bikes-ii/discuss/303422/Python-Priority-Queue

import heapq

class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        seen = set()
        h = [[0, 0, 0]]
        while True:
            cost, i, taken = heapq.heappop(h)
            if (i, taken) in seen:
                continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in xrange(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])

if __name__ == "__main__":
    sol = Solution()
    print sol.assignBikes([[0, 0], [1, 1], [2, 0]], [[1, 0], [2, 2], [2, 1]])
