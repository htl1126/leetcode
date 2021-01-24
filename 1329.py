class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i - j].pop()
        return mat

if __name__ == "__main__":
    sol = Solution()
    print(sol.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]))
