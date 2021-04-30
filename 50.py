# ref: https://discuss.leetcode.com/topic/15630/shortest-python-guaranteed/2
import sys


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        t, ans = x, 1
        while n:
            if n & 1:
                ans *= t
            t **= 2
            n >>= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.myPow(float(sys.argv[1]), int(sys.argv[2]))
