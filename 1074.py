# Ref: (original idea) https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum
# Ref: (speed up) https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/344440/Simple-Python-DP-solution

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # use the original matrix not reference vars to speed up
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
        ans = 0
        # use the original dict instead of collections.defaultdict to speedup
        for i in range(n):
            for j in range(i, n):
                count = {0: 1}
                cur = 0
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i - 1 >= 0 else 0)
                    ans += count.setdefault(cur - target, 0)
                    count[cur] = count.setdefault(cur, 0) + 1
        return ans
