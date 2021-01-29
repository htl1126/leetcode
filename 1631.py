# Ref: https://leetcode.com/problems/path-with-minimum-effort/discuss/909002/JavaPython-3-3-codes%3A-Binary-Search-Bellman-Ford-and-Dijkstra-w-brief-explanation-and-analysis.

import heapq

class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])
        effort = [[float('inf') for _ in range(n)] for _ in range(m)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            min_effort, x, y = heapq.heappop(heap)
            if (x, y) == (m - 1, n - 1):
                return min_effort
            for r, c in ((x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)):
                if m > r >= 0 <= c < n:
                    new_effort = max(min_effort, abs(heights[r][c] - heights[x][y]))
                    if new_effort < effort[r][c]:
                        effort[r][c] = new_effort
                        heapq.heappush(heap, (effort[r][c], r, c))

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
