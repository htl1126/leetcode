# Ref: https://leetcode.com/problems/sentence-similarity/discuss/109624/Simple-Python-Solution-32ms!

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        dic = collections.defaultdict(set)
        for a, b in similarPairs:
            dic[a].add(b)
            dic[b].add(a)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 != w2 and w1 not in dic[w2]:
                return False
        return True
