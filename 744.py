class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l < r:
            m = (l + r) // 2
            if ord(letters[m]) > ord(target):
                r = m
            else:
                l = m + 1
        if ord(letters[l]) > ord(target):
            return letters[l]
        return letters[0]
