# Ref: https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/918408/Python-5-lines-hashmap

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {p[0]: p for p in pieces}
        ans = []
        for n in arr:
            ans += d.get(n, [])
        return ans == arr
