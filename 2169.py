# Ref: https://leetcode.com/problems/count-operations-to-obtain-zero/discuss/1766803/JavaPython-3-Use-divmod-operation-w-explanation-and-analysis.

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while min(num1, num2) > 0:
            if num1 < num2:
                num1, num2 = num2, num1
            op, num1 = divmod(num1, num2)
            ans += op
        return ans
