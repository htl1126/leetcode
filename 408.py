import re


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        tokens = [t for t in re.split('(\D)', abbr) if t]
        cur = 0
        while tokens:
            t = tokens.pop(0)
            if t.isdigit():
                if t[0] == '0':
                    return False
                cur += int(t)
            else:
                if t != word[cur]:
                    return False
                cur += 1
            if cur >= len(word):
                break
        return cur == len(word) and not tokens
