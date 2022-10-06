# Ref: https://leetcode.com/problems/numbers-with-same-consecutive-differences/discuss/211183/JavaC%2B%2BPython-Iterative-BFS-Solution

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = range(1, 10)
        for _ in range(n - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + k, x % 10 - k] if 0 <= y <= 9}
        return list(cur)
