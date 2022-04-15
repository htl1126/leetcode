class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha_set = set()
        for c in sentence:
            alpha_set.add(c)
        return len(alpha_set) == 26
