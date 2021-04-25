# ref: https://discuss.leetcode.com/topic/8343/use-defaultdict-for-traceback-
#              and-easy-writing-20-lines-python-code
import collections


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        if endWord not in wordList:
            return []
        wordlist = set(wordList)
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        n = node[:i] + char + node[i + 1:]
                        if n in wordlist and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            t = []
            for r in res:
                for p in parents[r[0]]:
                    t.append([p] + r)
            res = t
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.findLadders('hit', 'cog', {"hot", "dot", "dog", "lot", "log"})
