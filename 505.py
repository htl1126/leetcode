# Ref: https://leetcode.com/problems/the-maze-ii/discuss/466603/Python-BFS-%2B-Heap
# Algo: BFS

import heapq

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        heap = [(0, start[0], start[1])]
        visited = {}
        r, c = len(maze), len(maze[0])
        while heap:
            for _ in xrange(len(heap)):
                dis, x0, y0 = heapq.heappop(heap)
                if x0 == destination[0] and y0 == destination[1]:
                    return dis
                visited[(x0, y0)] = 1
                for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    x, y = x0, y0
                    while 0 <= x + dx < r and 0 <= y + dy < c and maze[x + dx][y + dy] == 0:
                        x += dx
                        y += dy
                    if (x, y) not in visited:
                        d = abs(x - x0) + abs(y - y0)
                        heapq.heappush(heap, (dis + d, x, y))
        return -1

if __name__ == "__main__":
    sol = Solution()
    print sol.shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4])
