# Ref: https://leetcode.com/problems/sentence-similarity-ii/discuss/109755/SHORT-Python-DFS-with-explanation
# Algo: DFS

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        if len(words1) != len(words2):
            return False
        words, similar_words = defaultdict(set), {}
        [(words[w1].add(w2), words[w2].add(w1)) for w1, w2 in pairs]
        def dfs(word, root_word):
            if word in similar_words:
                return
            similar_words[word] = root_word
            [dfs(synonym, root_word) for synonym in words[word]]
        [dfs(word, word) for word in words]
        return all(similar_words.get(w1, w1) == similar_words.get(w2, w2) for w1, w2 in zip(words1, words2))

if __name__ == "__main__":
    sol = Solution()
    print sol.areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]])
