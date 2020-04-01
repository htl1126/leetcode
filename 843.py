# Ref: https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison

import collections

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        x = 0
        while x < 6:
            count = collections.Counter(list(''.join(wordlist)))
            guess = max(wordlist, key=lambda w: sum(count[c] for c in w))
            x = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == x]

    def match(self, w1, w2):
        return sum(i == j for i, j in zip(w1, w2))
