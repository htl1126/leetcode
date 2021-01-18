import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countVowelStrings(1))
