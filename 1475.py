# Ref: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/discuss/685390/JavaC%2B%2BPython-Stack-One-Pass

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                prices[stack.pop()] -= p
            stack.append(i)
        return prices
