# Ref: https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/1406774/Java-4-solutions-union-find-9ms-Union-by-Rank-14-ms-DFS-88-ms-BFS-90-ms

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        p = {}
        def find(x):
            p.setdefault(x, x)
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p[find(x)] = find(y)

        for e in edges:
            union(e[0], e[1])
        return find(source) == find(destination)
