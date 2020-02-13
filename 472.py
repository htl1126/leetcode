# Ref: https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution
# Algo: DFS and Dynamic Programming
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)
        def dfs(word):
            for i in xrange(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
