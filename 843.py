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

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n = 0
        while n < 6:
            count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
            guess = max(wordlist, key=lambda w: sum(count[i][c] for i, c in enumerate(w)))
            n = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == n]

    def match(self, w1, w2):
        return sum(i == j for i, j in zip(w1, w2))
