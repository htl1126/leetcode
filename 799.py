# Ref: https://leetcode.com/problems/champagne-tower/discuss/118711/JavaC%2B%2BPython-1D-DP-O(R)-space

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ans = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                # 1-d calculation uses backward updating
                ans[i] = max(ans[i] - 1, 0) / 2 + max(ans[i - 1] - 1, 0) / 2
        return min(1, ans[query_glass])
