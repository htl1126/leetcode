# Ref: https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += "+0"
        preOp, num, stack = "+", 0, []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if preOp == "+":
                    stack.append(num)
                elif preOp == "-":
                    stack.append(-num)
                elif preOp == "*":
                    stack.append(stack.pop() * num)
                elif preOp == "/":
                    n = stack.pop()
                    if n < 0:
                        stack.append(-(-n / num))
                    else:
                        stack.append(n / num)
                preOp, num = c, 0
        return sum(stack)

if __name__ == '__main__':
    sol = Solution()
    print sol.calculate('14-3/2')
