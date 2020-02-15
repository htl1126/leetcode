# Ref: https://leetcode.com/problems/number-of-distinct-islands/discuss/161867/Python-Very-Clean-and-Easy-to-Understand
# Algo: DFS

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(i, j, direct):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                self.steps += direct
                helper(i - 1, j, 'u')
                helper(i, j - 1, 'l')
                helper(i, j + 1, 'r')
                helper(i + 1, j, 'd')
                self.steps += 'b'
        distinctIslands = set()
        self.steps = ''
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    helper(i, j, 'o')
                    distinctIslands.add(self.steps)
                    self.steps = ''
        return len(distinctIslands)

if __name__ == "__main__":
    sol = Solution()
    print sol.numDistinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]])
