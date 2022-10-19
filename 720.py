# Ref: https://leetcode.com/problems/longest-word-in-dictionary/discuss/1412660/Python-3-solutions%3A-BFS-Sorting-TrieNode-Clean-and-Concise

class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = None
    def add(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.word = word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for w in words:
            root.add(w)

        q = collections.deque([root])
        ans = ""
        # use BFS to traverse the trie to find the longest "build path"
        # example:
        #   a - ap - app - appl - apple (we can go from "a" to "apple")
        #   a - ap - appl - apple       (we will stop at "ap" since word at node "app" is None)
        while q:
            node = q.popleft()
            for child in node.children.values():
                if child.word:
                    if len(child.word) > len(ans) or len(child.word) == len(ans) and child.word < ans:
                        ans = child.word
                    q.append(child)
        return ans
