# Ref: https://leetcode.com/problems/race-car/discuss/123834/JavaC%2B%2BPython-DP-solution

class Solution:
    dp = {0: 0}
    def racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]
        n = target.bit_length()
        if 2 ** n - 1 == target:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar(2 ** n - 1 - target) + n + 1
            for m in range(n - 1):
                self.dp[target] = min(self.dp[target], self.racecar(target - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[target]
