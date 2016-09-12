import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        vmap = collections.defaultdict(dict)
        for i in xrange(len(equations)):
            a, b = equations[i]
            v = values[i]
            vmap[a] = collections.defaultdict(dict) if not vmap[a] else vmap[a]
            vmap[b] = collections.defaultdict(dict) if not vmap[b] else vmap[b]
            vmap[a][a], vmap[a][b], vmap[b][a], vmap[b][b] = 1.0, v, 1 / v, 1.0
        ans = []

        def search(a, b, v, visited):
            if a not in vmap and b not in vmap:
                return -1.0
            if a == b:
                return v
            for t in vmap[a]:
                if t != a and t not in visited:
                    res = search(t, b, v, visited + [t])
                    if res > 0:
                        return v * vmap[a][t] * res
            return -1.0
        for qa, qb in queries:
            res = search(qa, qb, 1.0, [])
            ans.append(res if res > 0 else -1.0)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                           [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"],
                            ["x", "x"]])
