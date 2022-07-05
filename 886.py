# Ref: https://leetcode.com/problems/possible-bipartition/discuss/655842/Python-(Union-Find-DFS-BFS)-with-explanation

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        for i, j in dislikes:
            g[i].append(j)
            g[j].append(i)
        visited, mapping = set(), {}
            
        def dfs(i, group):
            if i in visited and mapping[i] != group:
                return False
            mapping[i] = group
            if i not in visited:
                visited.add(i)
                for j in g[i]:
                    if not dfs(j, not group):
                        return False
            return True
        
        for i in range(1, n + 1):
            if i not in visited:
                if not dfs(i, True):
                    return False
        return True
