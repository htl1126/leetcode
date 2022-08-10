# Ref: https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290858/JavaC%2B%2BPython-Greedily-Paint

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * n
        g = [[] for _ in range(n)]
        for i, j in paths:
            g[i - 1].append(j - 1)
            g[j - 1].append(i - 1)
        for i in range(n):
            ans[i] = ({1, 2, 3, 4} - {ans[j] for j in g[i]}).pop()
        return ans
