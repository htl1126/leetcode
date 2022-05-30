# Ref: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/discuss/648610/JavaPython-3-Straight-forward-codes.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s_list = sentence.split()
        sw_len = len(searchWord)
        for i, s in enumerate(s_list):
            if len(s) >= sw_len and s[:sw_len] == searchWord:
                return i + 1
        return -1
