# ref: https://discuss.leetcode.com/topic/8343/use-defaultdict-for-traceback-
#              and-easy-writing-20-lines-python-code
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordlist = set(wordList)
        level = {beginWord: None}
        # build a tree where the root is endWord and leaves are beginWord
        children = collections.defaultdict(set)
        while level and endWord not in children:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(beginWord)):
                        n = node[:i] + char + node[i + 1:]
                        if n in wordlist and n not in children:
                            next_level[n].add(node)
            level = next_level
            children.update(next_level)
        res = [[endWord]]
        # construct solutions from root to leaves
        while res and res[0][0] != beginWord:
            t = []
            for r in res:
                for p in children[r[0]]:
                    t.append([p] + r)
            res = t  # t will be empty if the tree is incomplete
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.findLadders('hit', 'cog', {"hot", "dot", "dog", "lot", "log"})
