class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        space_size = text.count(' ')
        if len(words) == 1:
            return words[0] + " " * space_size
        if space_size % (len(words) - 1) == 0:
            return (" " * (space_size // (len(words) - 1))).join(words)
        return (" " * (space_size // (len(words) - 1))).join(words) + " " * (space_size % (len(words) - 1))
