# Ref: https://leetcode.com/problems/design-search-autocomplete-system/discuss/105386/Python-Clean-Solution-Using-Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None
        self.score = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        for sentence, score in zip(sentences, times):
            self.add_record(sentence, score)

    def add_record(self, sentence, score):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_end = True
        p.data = sentence
        p.score -= score  # newly added sentences might already existed

    def search(self, s):
        p = self.root
        for c in s:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)

    def dfs(self, node):
        result = []
        if node:
            if node.is_end:
                result.append((node.score, node.data))
            for child in node.children:
                result += self.dfs(node.children[child])
        return result

    def input(self, c: str) -> List[str]:
        result = []
        if c != '#':
            self.keyword += c
            result = self.search(self.keyword)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""
        print(result)
        return [item[1] for item in sorted(result)[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
