# ref: https://discuss.leetcode.com/topic/26944/python-solution
#              -recursive-version-dfs


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dic = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.dic
        for c in word:
            node = node.setdefault(c, {})
        node['end'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
         """
        return self.searchWord(self.dic, word)

    def searchWord(self, node, word):
        n = node
        for i in xrange(len(word)):
            if word[i] == '.':
                for char in n:
                    if char != 'end':
                        if self.searchWord(n[char], word[i + 1:]):
                            return True
                return False
            else:
                if word[i] in n:
                    n = n[word[i]]
                else:
                    return False
        if 'end' in n:
            return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

if __name__ == '__main__':
    wordDic = WordDictionary()
    wordDic.addWord('at')
    wordDic.addWord('and')
    wordDic.addWord('an')
    wordDic.addWord('add')
    print wordDic.search('a')
    print wordDic.search('.at')
    wordDic.addWord('bat')
    print wordDic.search('.at')
