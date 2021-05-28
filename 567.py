class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        size_s1 = len(s1)
        c_s1, c_s2 = collections.Counter(s1), collections.Counter(s2[:size_s1 - 1])
        for i in range(size_s1 - 1, len(s2)):
            c_s2[s2[i]] += 1
            if c_s1 == c_s2:
                return True
            c_s2[s2[i - size_s1 + 1]] -= 1
            if c_s2[s2[i - size_s1 + 1]] == 0:
                del c_s2[s2[i - size_s1 + 1]]
        return False
