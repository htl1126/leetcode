# Ref: https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/1907109/PythonDP-easy-to-understand

class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {"1": 0, "0": 0, "10": 0, "01": 0, "101": 0, "010": 0}
        for c in s:
            if c == '1':
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
            else:
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
        return dp["010"] + dp["101"]
