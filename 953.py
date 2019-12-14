class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

if __name__ == "__main__":
    sol = Solution()
    print sol.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")

# Algorithm: ad-hoc
# Ref: https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185
# Hint: Python can directly compare list of numbers
