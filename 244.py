# ref: https://discuss.leetcode.com/topic/48368/short-n-clean-o-n-init-o-n-query
#              -in-python


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.d = {}
        for i, w in enumerate(words):
            self.d[w] = self.d.get(w, []) + [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        a, b = self.d[word1], self.d[word2]
        m, n, i, j, res = len(a), len(b), 0, 0, float('inf')
        while i < m and j < n:
            res = min(res, abs(a[i] - b[j]))
            if a[i] > b[j]:
                j += 1
            else:
                i += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

if __name__ == '__main__':
    wordD = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print wordD.shortest('coding', 'practice')
