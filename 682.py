# ref: https://leetcode.com/problems/baseball-game/solutions/607494/easy-to-understand-faster-simple-stack-based-python-solution

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0

        for op in operations:
            if op == "C":
                ans -= stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
                ans += stack[-1]
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
                ans += stack[-1]
            else:
                stack.append(int(op))
                ans += stack[-1]

        return ans

