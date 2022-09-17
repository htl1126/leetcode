# Ref: https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1671908/Python-3-or-Math-or-Explanation

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        row1, row1_inverted = grid[0], [1 - v for v in grid[0]]
        for i in range(len(grid)):
            if grid[i] != row1 and grid[i] != row1_inverted:
                return False
        return True
