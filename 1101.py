# Ref: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/discuss/322961/Python-Union-Find

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        p = {}
        self.groups = n

        def find(x):
            p.setdefault(x, x)
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.groups -= 1
                p[x] = y

        for t, u, v in sorted(logs):
            union(u, v)
            if self.groups == 1:
                return t
        return -1
