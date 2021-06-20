# Ref: https://leetcode.com/problems/implement-magic-dictionary/discuss/107454/Python-without-*26-factor-in-complexity

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = None
        self.near = None

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.near = collections.Counter(w[:i] + '*' + w[i + 1:] for w in self.words for i in range(len(w)))

    def search(self, searchWord: str) -> bool:
        return any(self.near[w] > 1 or self.near[w] == 1 and searchWord not in self.words for w in [searchWord[:i] + '*' + searchWord[i + 1:] for i in range(len(searchWord))])


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
