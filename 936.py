# Ref: https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m, s, t = len(target), len(stamp), list(stamp), list(target)
        ans = []
        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?':
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                ans.append(i)
            return changed
        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        return ans[::-1] if t == ['?'] * n else []
