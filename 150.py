# ref: https://leetcode.com/discuss/4076/6-%EF%BC%88-132%EF%BC%89-0-or-1


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token.isdigit() or token[0] == '-' and token[1:].isdigit():
                stack.append(token)
            else:
                op2, op1 = stack.pop(), stack.pop()
                if token == '/':
                    stack.append(int(float(op1) / int(op2)))
                else:
                    stack.append(eval('{0} {1} {2}'.format(op1, token, op2)))
        return int(stack[0])

if __name__ == '__main__':
    sol = Solution()
    print sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
