# Ref: https://leetcode.com/problems/sort-integers-by-the-power-value/discuss/546747/Python-Sort-and-Cache

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {1: 0}
        def compute(i):
            if i not in dic:
                if i % 2:
                    dic[i] = compute(i * 3 + 1) + 1
                else:
                    dic[i] = compute(i // 2) + 1
            return dic[i]
        return sorted((compute(i), i) for i in range(lo, hi + 1))[k - 1][1]
