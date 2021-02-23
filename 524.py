# Ref: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/discuss/99590/Short-Python-solutions

class Solution:
    def findLongestWord(self, s, d) -> str:
        for x in sorted(d, key=lambda x: (-len(x), x)):
            it = iter(s)
            if all(c in it for c in x):
                return x
        return ""

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
