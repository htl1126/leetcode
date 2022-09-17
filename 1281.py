class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        while n:
            t = n % 10
            p *= t
            s += t
            n //= 10
        return p - s
