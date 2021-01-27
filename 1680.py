class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, M = 0, 10 ** 9 + 7
        for n in range(1, n + 1):
            ans = (ans * (1 << (len(bin(n)) - 2)) + n) % M
        return ans
