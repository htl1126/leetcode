# ref: https://leetcode.com/discuss/48083/share-python-solutions-concise
#              -160ms-optimized-solution-100ms


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        length = 2
        size = len(beginWord)
        front = set([beginWord])
        back = set([endWord])
        wordList = set(wordList)
        wordList.discard(beginWord)
        while front:
            front = wordList & set(w[:i] + c + w[i + 1:] for w in front for i in range(size)
                                   for c in 'abcdefghijklmnopqrstuvwxyz')
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
