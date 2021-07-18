# ref: https://leetcode.com/problems/uncommon-words-from-two-sentences/discuss/158967/C%2B%2BJavaPython-Easy-Solution-with-Explanation

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = collections.Counter((s1 + " " + s2).split())
        return [w for w in c if c[w] == 1]
