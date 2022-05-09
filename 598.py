# Ref: https://leetcode.com/problems/range-addition-ii/discuss/1434377/Python-oneliner-explained

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(i for i, _ in ops + [[m, n]]) * min(j for _, j in ops + [[m, n]])
