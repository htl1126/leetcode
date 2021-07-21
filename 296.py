# ref: https://discuss.leetcode.com/topic/27746/3-8-lines-o-mn-python


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        total = 0
        # We get each row of the grid and each column of the grid
        for grid in grid, zip(*grid):  # zip(*grid): rotate the grid with 90 degrees
            X = []
            for x, row in enumerate(grid):
                X += [x] * sum(row)
            for x in X:
                # calculate the minimum sum of distances from the median to all the points
                total += abs(x - X[len(X) // 2])
        return total

if __name__ == '__main__':
    sol = Solution()
    print sol.minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0]])
