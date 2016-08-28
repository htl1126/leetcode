class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        board = [[0] * n for _ in xrange(n)]
        dis, step = [[0, 1], [1, 0], [0, -1], [-1, 0]], 0
        for num in xrange(1, n * n + 1):
            board[i][j] = num
            if not(0 <= i + dis[step][0] < n and 0 <= j + dis[step][1] < n and
                   not board[i + dis[step][0]][j + dis[step][1]]):
                step = (step + 1) % 4
            i += dis[step][0]
            j += dis[step][1]
        return board

if __name__ == '__main__':
    sol = Solution()
    print sol.generateMatrix(4)
