# Ref: https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        count = collections.Counter()
        for b in B:
            count |= collections.Counter(b)
        return [a for a in A if not count - collections.Counter(a)]
