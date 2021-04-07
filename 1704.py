class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = list("aeiouAEIOU")
        left, right = s[:len(s) // 2], s[len(s) // 2:]
        return sum(left.count(v) for v in vowels) == sum(right.count(v) for v in vowels)
