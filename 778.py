# Ref: https://leetcode.com/problems/swim-in-rising-water/discuss/113770/C%2B%2BPython-PriorityQueue

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, q, seen, ans = len(grid), [(grid[0][0], 0, 0)], set([(0,0)]), 0
        while True:
            t, i, j = heapq.heappop(q)
            ans = max(ans, t)
            if i == j == n - 1:
                return ans
            for x, y in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    heapq.heappush(q, (grid[x][y], x, y))
