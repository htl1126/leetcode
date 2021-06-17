class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y, dx, dy, ans = 0, 0, 0, 1, []
        m, n = len(matrix), len(matrix[0])
        for _ in range(m * n):
            ans.append(matrix[x][y])
            matrix[x][y] = 101  # -100 <= matrix[x][y] <= 100
            if not(0 <= x + dx < m and 0 <= y + dy < n and matrix[x + dx][y + dy] != 101):
                dx, dy = dy, -dx
            x, y = x + dx, y + dy
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
