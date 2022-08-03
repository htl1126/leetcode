# Ref: https://leetcode.com/problems/string-matching-in-an-array/discuss/577564/Python3-Simple-Code
# Ref: https://stackoverflow.com/questions/35855748/whats-the-computational-cost-of-count-operation-on-strings-python

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ' '.join(words)
        return [w for w in words if s.count(w) >= 2]
