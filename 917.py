class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        t = list(s)
        while l < r:
            while not t[l].isalpha() and l < r:
                l += 1
            while not t[r].isalpha() and l < r:
                r -= 1
            t[l], t[r] = t[r], t[l]
            l, r = l + 1, r - 1
        return "".join(t)
