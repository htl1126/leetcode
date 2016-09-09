# ref: https://discuss.leetcode.com/topic/27746/3-8-lines-o-mn-python


class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        for grid in grid, zip(*grid):
            X = []
            for x, row in enumerate(grid):
                X += [x] * sum(row)
            total += sum(abs(x - X[len(X) / 2]) for x in X)
        return total

if __name__ == '__main__':
    sol = Solution()
    print sol.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0]])
