# Ref: https://leetcode.com/problems/the-maze/discuss/150523/Python-elegant-DFS-solution
# Algo: DFS

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        r, c, stopped = len(maze), len(maze[0]), set()
        def traverse(pos):
            x, y = pos[0], pos[1]
            if (x, y) in stopped:
                return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                new_x, new_y = x, y
                while 0 <= new_x + dx < r and 0 <= new_y + dy < c and maze[new_x + dx][new_y + dy] != 1:
                    new_x += dx
                    new_y += dy
                if traverse([new_x, new_y]):
                    return True
            return False
        return traverse(start)

if __name__ == "__main__":
    sol = Solution()
    print sol.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4])
