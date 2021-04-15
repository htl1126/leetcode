class Solution:
    def fib(self, n: int) -> int:
        f = [0] * 31
        f[1] = 1
        for i in range(2, 31):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
