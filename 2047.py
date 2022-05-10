# Ref: https://leetcode.com/problems/number-of-valid-words-in-a-sentence/discuss/1537625/Python3-check-words

class Solution:
    def countValidWords(self, sentence: str) -> int:
        def check_word(w):
            seen = False
            for i, c in enumerate(w):
                if c.isdigit() or c in "!.," and i != len(w) - 1:
                    return False
                if c == '-':
                    if seen or i == 0 or i == len(w) - 1 or not w[i + 1].isalpha():
                        return False
                    seen = True
            return True
        return sum(check_word(w) for w in sentence.split())
