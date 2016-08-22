# ref: https://discuss.leetcode.com/topic/15806/easy-18-lines-c-16-lines-python


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        total, signs, i = 0, [1, 1], 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '(+-':
                if c == '-':
                    signs.append(-signs[-1])
                else:
                    signs.append(signs[-1])
            elif c == ')':
                signs.pop()
            i += 1
        return total

if __name__ == '__main__':
    sol = Solution()
    print sol.calculate('(1+(4+5+2)-3)+(6+8)')
