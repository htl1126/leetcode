# Ref: https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for c in S:
            if c.isalpha():
                res = [i + j for i in res for j in [c.lower(), c.upper()]]
            else:
                res = [i + c for i in res]
        return res
