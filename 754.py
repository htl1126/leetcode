# Ref: https://leetcode.com/problems/reach-a-number/discuss/112986/Concise-Python-with-explanation-and-example

import math

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = math.floor(math.sqrt(target * 2))
        while True:
            diff = (n + 1) * n / 2 - target
            if diff >= 0 and diff % 2 == 0:
                return int(n)
            n += 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.reachNumber(2))
