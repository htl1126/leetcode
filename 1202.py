# Ref: https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = {}

        def find(x):
            p.setdefault(x, x)
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            p[find(x)] = find(y)

        ans = []
        d = collections.defaultdict(list)
        for x, y in pairs:
            union(x, y)
        for i in range(len(s)):
            d[find(i)].append(s[i])
        for i in d.keys():
            d[i].sort(reverse=True)
        for i in range(len(s)):
            ans.append(d[find(i)].pop())
        return ''.join(ans)
