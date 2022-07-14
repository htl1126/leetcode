# Ref: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927522/Python-n-log-n-690-ms

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        d = sorted(collections.Counter(inventory).items(), reverse=True) + [(0, 0)]
        ans, width, i = 0, 0, 0

        while orders > 0:
            width += d[i][1]
            sell = min(orders, width * (d[i][0] - d[i + 1][0]))
            whole, remainder = divmod(sell, width)
            ans += ((d[i][0] + (d[i][0] - whole + 1)) * whole // 2) * width + remainder * (d[i][0] - whole)
            orders -= sell
            i += 1
        return ans % (10 ** 9 + 7)
