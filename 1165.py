class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        prev, cur = -1, 0
        ans = 0
        for c in word:
            prev, cur = cur, keyboard.index(c)
            ans += abs(prev - cur)
        return ans
