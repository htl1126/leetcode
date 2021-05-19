# Ref: https://leetcode.com/problems/basic-calculator-iii/discuss/127881/Python-O(n)-Solution-using-recursion

class Solution:
    def calculate(self, s: str) -> int:
        stack, num, op = [], 0, '+'
        for i, c in enumerate(s + '+'):
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '(':
                stack.append(op)
                stack.append('(')
                op = '+'
            elif c in "+-*/)":
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                if c == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    op = stack.pop()
                else:
                    op, num = c, 0
        return sum(stack)
