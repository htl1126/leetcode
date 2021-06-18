# ref: https://discuss.leetcode.com/topic/26944/python-solution
#              -recursive-version-dfs


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def addWord(self, word: str) -> None:
        node = self.dic
        for c in word:
            node = node.setdefault(c, {})
        node['end'] = True

    def search(self, word: str) -> bool:
        return self.searchWord(self.dic, word)
    
    def searchWord(self, node, word):
        if word == '':
            return 'end' in node
        if word[0] == '.':
            for c in node:
                if c != 'end' and self.searchWord(node[c], word[1:]):
                    return True
        else:
            if word[0] in node:
                return self.searchWord(node[word[0]], word[1:])
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
