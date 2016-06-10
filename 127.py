# ref: https://leetcode.com/discuss/48083/share-python-solutions-concise
#              -160ms-optimized-solution-100ms


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        length = 2
        front = set([beginWord])
        back = set([endWord])
        wordList.discard(beginWord)
        while front:
            front = wordList & set(
                '{0}{1}{2}'.format(
                    word[:index], ch, word[index + 1:]
                ) for word in front for index in xrange(
                    len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz')
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            wordList -= front
        return 0

if __name__ == '__main__':
    sol = Solution()
    print sol.ladderLength('hit', 'cog', set(["hot", "dot", "dog",
                                              "lot", "log"]))
