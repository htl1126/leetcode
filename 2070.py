# Ref: https://leetcode.com/problems/most-beautiful-item-for-each-query/discuss/1576050/Python-4-lines-Solution
# Ref: https://leetcode.com/problems/most-beautiful-item-for-each-query/discuss/1575928/Java-or-TreeMap-or-BinarySearch-or-similar-problems

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items + [[0, 0]])
        for i in range(len(items) - 1):
            items[i + 1][1] = max(items[i][1], items[i + 1][1])
        ans = []
        for q in queries:
            l, r = 0, len(items) - 1
            while l < r:
                m = (l + r + 1) // 2
                if items[m][0] <= q:
                    l = m
                else:
                    r = m - 1
            ans.append(items[l][1])
        return ans
