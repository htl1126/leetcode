# Ref: https://leetcode.com/problems/rotting-oranges/discuss/238540/python-simple-bfs-solution
# Algo: BFS
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def createSet(grid, targetVal):
            result = set()
            for x in xrange(len(grid)):
                for y in xrange(len(grid[0])):
                    if grid[x][y] == targetVal:
                        result.add((x, y))
            return result

        rotten = createSet(grid, 2)
        fresh = createSet(grid, 1)
        time = 0
        while len(fresh):
            turned = set()
            for x, y in fresh:
                if (x - 1, y) in rotten or (x, y - 1) in rotten or (x, y + 1) in rotten or (x + 1, y) in rotten:
                    turned.add((x, y))
            if len(turned) == 0:
                return -1
            fresh.difference_update(turned)
            rotten.update(turned)
            time += 1
        return time

if __name__ == "__main__":
    sol = Solution()
