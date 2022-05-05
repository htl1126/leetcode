# Ref: https://leetcode.com/problems/find-common-characters/discuss/247560/Python-1-Line

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = collections.Counter(words[0])
        for i in range(1, len(words)):
            ans &= collections.Counter(words[i])
        return list(ans.elements())
