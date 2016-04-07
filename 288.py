class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.lookup = collections.defaultdict(set)
        for word in dictionary:
            if len(word) > 2:
                new_word = '{0}{1}{2}'.format(word[0], len(word) - 2, word[-1])
            else:
                new_word = word
            self.lookup[new_word].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) > 2:
            new_word = '{0}{1}{2}'.format(word[0], len(word) - 2, word[-1])
        else:
            new_word = word
        return new_word not in self.lookup or self.lookup[new_word] == set([word])
