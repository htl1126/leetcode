# ref: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-concise-solution-with-memorization


class Solution:
    def diffWaysToCompute(self, expression: str, memo={}) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        if expression not in memo:
            res = []
            for i in range(len(expression)):
                if expression[i] in "-+*":
                    res1 = self.diffWaysToCompute(expression[:i], memo)
                    res2 = self.diffWaysToCompute(expression[i + 1:], memo)
                    for x in res1:
                        for y in res2:
                            op = expression[i]
                            if op == "+":
                                res.append(x + y)
                            elif op == "-":
                                res.append(x - y)
                            else:
                                res.append(x * y)
            memo[expression] = res
        return memo[expression]

if __name__ == '__main__':
    sol = Solution()
    print sol.diffWaysToCompute('2*3-4*5')
