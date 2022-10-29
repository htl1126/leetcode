# Ref: https://leetcode.com/problems/detonate-the-maximum-bombs/discuss/1623311/Python-Simple-dfs-explained

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, ans, g = len(bombs), 0, collections.defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i != j:
                    if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                        g[i].append(j)

        visited = set()
        def dfs(i):
            for j in g[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)

        ans = 0
        for i in range(n):
            visited = set([i])
            dfs(i)
            ans = max(ans, len(visited))
        return ans
