# Ref: https://leetcode.com/problems/global-and-local-inversions/discuss/113644/C%2B%2BJavaPython-Easy-and-Concise-Solution

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        cmax = -1
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True
