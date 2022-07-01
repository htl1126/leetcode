class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r, c = len(img), len(img[0])
        ans = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                t = size = 0
                for x in range(-1, 2, 1):
                    for y in range(-1, 2, 1):
                        if 0 <= i + x < r and 0 <= j + y < c:
                            t += img[i + x][j + y]
                            size += 1
                ans[i][j] = t // size
        return ans
