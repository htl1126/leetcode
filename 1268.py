# Ref: https://leetcode.com/problems/search-suggestions-system/discuss/509506/Python-Trie-with-explanation
# Algo: trie

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.top3 = []

    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.top3.append(word)
            cur.top3.sort()
            if len(cur.top3) > 3:
                cur.top3.pop()

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        root = TrieNode()
        for p in products:
            root.insert(p)

        node, ans, end = root, [], False
        for c in searchWord:
            if end or c not in node.children:
                ans.append([])
                end = True
            else:
                node = node.children[c]
                ans.append(node.top3)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
