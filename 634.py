# Ref: https://leetcode.com/problems/find-the-derangement-of-an-array/discuss/104981/If-you-don't-understand
# Ref: https://leetcode.com/problems/find-the-derangement-of-an-array/discuss/104986/Python-Straightforward-with-Explanation

class Solution:
    def findDerangement(self, n: int) -> int:
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = b, (i - 1) * (a + b) % (10 ** 9 + 7)
        return b
