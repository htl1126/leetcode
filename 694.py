# Ref: https://leetcode.com/problems/number-of-distinct-islands/discuss/161867/Python-Very-Clean-and-Easy-to-Understand
# Algo: DFS

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def helper(i, j, direct):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0  # we don't want to visit the same island twice
                self.steps += direct
                helper(i - 1, j, 'u')
                helper(i, j - 1, 'l')
                helper(i, j + 1, 'r')
                helper(i + 1, j, 'd')
                self.steps += 'b'  # this line is important
        distinctIslands = set()
        self.steps = ''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    helper(i, j, 'o')
                    distinctIslands.add(self.steps)
                    self.steps = ''
        return len(distinctIslands)

if __name__ == "__main__":
    sol = Solution()
    print sol.numDistinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]])
