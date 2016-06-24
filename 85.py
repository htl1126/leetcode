# ref: https://leetcode.com/discuss/20240/share-my-dp-solution


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        left = [0 for _ in xrange(col)]
        right = [col for _ in xrange(col)]
        height = [0 for _ in xrange(col)]
        ans = 0
        for i in xrange(row):
            cur_left, cur_right = 0, col
            for j in xrange(col):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in xrange(col):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j], cur_left = 0, j + 1
            for j in xrange(col - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j], cur_right = col, j
            for j in xrange(col):
                ans = max(ans, (right[j] - left[j]) * height[j])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.maximalRectangle(['11111', '00011'])
