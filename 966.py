# Ref: https://leetcode.com/problems/vowel-spellchecker/discuss/211189/JavaC%2B%2BPython-Two-HashMap

import re

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        words = {w: w for w in wordlist}
        cap = {w.lower(): w for w in wordlist[::-1]}
        vowel = {re.sub("[aeiou]", "#", w.lower()): w for w in wordlist[::-1]}
        return [words.get(q) or cap.get(q.lower()) or vowel.get(re.sub("[aeiou]", "#", q.lower()), "") for q in queries]

if __name__ == "__main__":
    sol = Solution()
    print sol.spellchecker(["KiTe", "kite", "hare", "Hare"], ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"])
