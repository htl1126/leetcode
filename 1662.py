class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.arrayStringAreEqual(["ab", "c"], ["a", "bc"]))
