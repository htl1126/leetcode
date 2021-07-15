# ref: https://leetcode.com/problems/number-of-atoms/discuss/140802/Python-20-lines-very-readable-simplest-and-shortest-solution-36-ms-beats-100

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d, coeff, num, p, stack, atom = collections.defaultdict(int), 1, 0, 0, [], ""
        for c in formula[::-1]:
            if c.isdigit():
                num += int(c) * (10 ** p)
                p += 1
            elif c == ')':
                if num:
                    stack.append(num)
                    coeff *= num
                else:
                    stack.append(1)
                num = p = 0
            elif c == '(':
                coeff //= stack.pop()
            elif c.isupper():
                atom += c
                d[atom[::-1]] += (num or 1) * coeff
                atom = ""
                num = p = 0
            elif c.islower():
                atom += c
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(d.items()))
