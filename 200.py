# https://leetcode.com/discuss/41509/7-lines-python-14-lines-java


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) \
                    and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i - 1, i + 1, i, i), (j, j, j - 1, j + 1))
                return 1
            return 0
        return sum(sink(i, j) for i in xrange(
            len(grid)) for j in xrange(len(grid[0])))

if __name__ == '__main__':
    sol = Solution()
    print sol.numIslands([list('11110'), list('11010'), list('11000'),
                          list('00000')])
