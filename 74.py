# ref: https://discuss.leetcode.com/topic/10211/a-python-binary-search-solution
#              -o-logn


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        lo, hi = 0, row * col - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            num = matrix[mid / col][mid % col]
            if num < target:
                lo = mid + 1
            elif num > target:
                hi = mid - 1
            else:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]],
                           16)
