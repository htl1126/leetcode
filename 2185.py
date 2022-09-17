class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w[:len(pref)] == pref for w in words)
