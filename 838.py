# Ref: https://leetcode.com/problems/push-dominoes/discuss/132332/JavaC%2B%2BPython-Two-Pointers

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = 'L' + dominoes + 'R'
        ans, i = "", 0
        for j in range(1, len(d)):
            if d[j] == '.':
                continue
            m = j - i - 1  # number of dominoes on the left to be processed
            if i:  # just add the previous processed 'L' or 'R'
                ans += d[i]
            if d[i] == d[j]:  # fall to the same direction
                ans += d[i] * m
            elif d[i] == 'L' and d[j] == 'R':  # d[i] falls to left and d[j] falls to right
                ans += '.' * m
            else:  # d[i] falls to right and d[j] falls to left
                ans += 'R' * (m // 2) + '.' * (m % 2) + 'L' * (m // 2)
            i = j  # update i
        return ans
