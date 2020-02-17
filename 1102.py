# Ref: https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/416227/Python-Dijkstra-Binary-Search-%2B-DFS-Union-Find-complexity-analysis
# Algo: DFS & binary search

import heapq

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        r, c = len(A), len(A[0])
        maxHeap = [(-A[0][0], 0, 0)]
        visited = [[0 for _ in xrange(c)] for _ in xrange(r)]
        while maxHeap:
            val, x, y = heapq.heappop(maxHeap)
            if x == r - 1 and y == c - 1:
                return -val
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    heapq.heappush(maxHeap, (max(val, -A[nx][ny]), nx, ny))
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.maximumMinimumPath([[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7], [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]])
