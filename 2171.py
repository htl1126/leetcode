# Ref: https://leetcode.com/problems/removing-minimum-number-of-magic-beans/discuss/1766795/JavaPython-3-Sort-then-1-pass-find-max-rectangle-w-graph-explanation-and-analysis.

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        max_sum, n = 0, len(beans)
        for i, bean in enumerate(sorted(beans)):
            max_sum = max(max_sum, bean * (n - i))
        return sum(beans) - max_sum
