# Ref: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/discuss/1329445/An-analysis-on-Time-Limit-Exceeded-(TLE)

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        r, c, q, ans = len(maze), len(maze[0]), [entrance], 0
        maze[entrance[0]][entrance[1]] = '+'
        while q:
            new_q = []
            for i, j in q:
                for x, y in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    if 0 <= i + x < r and 0 <= j + y < c and maze[i + x][j + y] == '.':
                        if i + x in [0, r - 1] or j + y in [0, c - 1]:
                            return ans + 1
                        new_q.append([i + x, j + y])
                        maze[i + x][j + y] = '+'  # must do the mark here
            q, ans = new_q, ans + 1
        return -1
