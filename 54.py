class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        row, col = len(matrix), len(matrix[0])
        displace = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direct_now = 0
        x, y = 0, -1
        result = [0 for _ in xrange(row * col)]
        length = row * col
        pos = 0
        while 1:
            displace_x, displace_y = displace[direct_now]
            if 0 <= x + displace_x < row and 0 <= y + displace_y < col and \
                    matrix[x + displace_x][y + displace_y] != None:
                x += displace_x
                y += displace_y
                result[pos] = matrix[x][y]
                matrix[x][y] = None
                pos += 1
                if pos == length:
                    return result
            else:
                direct_now = (direct_now + 1) % 4

if __name__ == '__main__':
    sol = Solution()
    print sol.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
