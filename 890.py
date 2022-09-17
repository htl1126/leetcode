# Ref: https://leetcode.com/problems/find-and-replace-pattern/discuss/161288/C%2B%2BJavaPython-Normalise-Word

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def F(w):
            m = {}
            return [m.setdefault(c, len(m)) for c in w]
        f_p = F(pattern)
        return [w for w in words if F(w) == f_p]
