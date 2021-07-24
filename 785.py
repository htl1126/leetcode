# Ref: https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color, n = {}, len(graph)
        
        def dfs(n):
            for i in graph[n]:
                if i in color:
                    if color[i] == color[n]:
                        return False
                else:
                    color[i] = 1 - color[n]
                    if not dfs(i):
                        return False
            return True
        
        for i in range(n):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
