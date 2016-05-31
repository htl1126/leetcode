# ref: https://leetcode.com/discuss/76907/python-dfs-bfs-union-find-solutions


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(v, g, visited):
            if visited[v]:
                return
            visited[v] = True
            for u in g[v]:
                dfs(u, g, visited)

        visited = [False for _ in xrange(n)]
        g = {x: [] for x in xrange(n)}
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = 0
        for v in xrange(n):
            if not visited[v]:
                dfs(v, g, visited)
                ans += 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.countComponents(5, [[0, 1], [1, 2], [3, 4]])
