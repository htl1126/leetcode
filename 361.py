# ref: https://discuss.leetcode.com/topic/48566/short-o-mn-python


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def hits(grid):
            hitmap = []
            for row in grid:
                hitmap_row = []
                blocks = ''.join(row).split('W')
                for block in blocks:
                    hitmap_row += [block.count('E')] * len(block) + [0]
                hitmap.append(hitmap_row)
            return hitmap
        rowhits = hits(grid)
        colhits = zip(*hits(zip(*grid)))
        max_kill = 0
        for row in zip(grid, rowhits, colhits):
            for cell, rh, ch in zip(*row):
                if cell == '0' and rh + ch > max_kill:
                    max_kill = rh + ch
        return max_kill

if __name__ == '__main__':
    sol = Solution()
    print sol.maxKilledEnemies([list('0E00'), list('E0WE'), list('0E00')])
