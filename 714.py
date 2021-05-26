# Ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/201603/Python.-Greedy-is-good.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 1:
            return 0
        minimum, ans = prices[0], 0
        for i in range(1, n):
            # looking for a new profit interval
            if prices[i] < minimum:
                minimum = prices[i]
            # stay in the same profit interval and update the profit
            elif prices[i] > minimum + fee:
                ans += prices[i] - minimum - fee
                minimum = prices[i] - fee
        return ans
