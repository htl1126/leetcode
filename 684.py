class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = {}
        def find(x):
            p.setdefault(x, x)
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            p[find(x)] = find(y)
            
        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            union(u, v)
