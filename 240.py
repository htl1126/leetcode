# ref: https://discuss.leetcode.com/topic/19496/4-lines-c-6-lines-ruby-7-lines
#              -python-1-liners/2


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        j = -1
        for row in matrix:
            while j + len(row) and row[j] > target:
                j -= 1
            if row[j] == target:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19],
                            [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
                            [18, 21, 23, 26, 30]], 27)
