class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        r, c = len(image), len(image[0])
        visited = [[False for _ in xrange(c)] for _ in xrange(r)]
        oldColor = image[sr][sc]
        def fill(x, y):
            image[x][y] = newColor
            visited[x][y] = True
            for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and image[nx][ny] == oldColor and not visited[nx][ny]:
                    fill(nx, ny)
        fill(sr, sc)
        return image
        
if __name__ == "__main__":
    sol = Solution()
    print sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
