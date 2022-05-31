# Ref: https://leetcode.com/problems/shopping-offers/discuss/105204/Python-dfs-with-memorization.

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n, d = len(needs), {}
        special = list(filter(lambda x: all(needs[i] >= x[i] for i in range(n)), special))
        def search(cur):
            val = sum(price[i] * cur[i] for i in range(n))
            for offer in special:
                if offer[-1] > val:
                    continue
                diff = [cur[i] - offer[i] for i in range(n)]
                if min(diff) >= 0:
                    val = min(val, d.get(tuple(diff), search(diff)) + offer[-1])
            d[tuple(cur)] = val
            return val
        return search(needs)
