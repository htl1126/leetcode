# ref: https://discuss.leetcode.com/topic/19496/4-lines-c-6-lines-ruby-7-lines
#              -python-1-liners/2


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        j = n - 1
        for i in range(m):
            while j >= 0 and target <= matrix[i][j]:
                if target == matrix[i][j]:
                    return True
                j -= 1
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],
                            [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
                            [18, 21, 23, 26, 30]], 27)
