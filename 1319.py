# Ref: https://leetcode.com/problems/number-of-operations-to-make-network-connected/discuss/477679/Python-Count-the-Connected-Networks

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        g = [set() for _ in range(n)]
        visited, n_subn = [False] * n, 0
        for e in connections:
            g[e[0]].add(e[1])
            g[e[1]].add(e[0])
        def dfs(i):
            visited[i] = True
            for j in g[i]:
                if not visited[j]:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                n_subn += 1
        return n_subn - 1
