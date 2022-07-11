# Ref: https://leetcode.com/problems/sum-of-square-numbers/discuss/1424957/Python-3-solutions%3A-Sqrt-HashSet-Two-Pointers-Clean-and-Concise-O(sqrt(c))

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while l <= r:
            cur = l * l + r * r
            if cur == c:
                return True
            if cur < c:
                l += 1
            else:
                r -= 1
        return False
