# Ref: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        for i, j in stones:
            union(i, ~j)
        return len(stones) - len({find(x) for x in UF})
