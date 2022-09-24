# Ref: https://leetcode.com/problems/construct-quad-tree/discuss/195855/Python-very-simple-recursive-solution-beats-97

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        def is_leaf(grid):
            return all(grid[i][j] == grid[0][0] for i in range(len(grid)) for j in range(len(grid[0])))
        if is_leaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node(-1,
                    False,
                    self.construct([row[:n // 2] for row in grid[:n // 2]]),
                    self.construct([row[n // 2:] for row in grid[:n // 2]]),
                    self.construct([row[:n // 2] for row in grid[n // 2:]]),
                    self.construct([row[n // 2:] for row in grid[n // 2:]]))
