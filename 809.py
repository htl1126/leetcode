# Ref: https://leetcode.com/problems/expressive-words/discuss/122660/C%2B%2BJavaPython-2-Pointers-and-4-pointers

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ans, s_len = 0, len(S)
        for w in words:
            found = False
            i, j, i2, j2, w_len = 0, 0, 0, 0, len(w)
            while i < s_len and j < w_len:
                if S[i] != w[j]:
                    break
                while i2 < s_len and S[i] == S[i2]:
                    i2 += 1
                while j2 < w_len and w[j] == w[j2]:
                    j2 += 1
                if i2 - i != j2 - j and (i2 - i < j2 - j or i2 - i < 3):
                    break
                i, j = i2, j2
            if i == s_len and j == w_len:
                ans += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.expressiveWords("heeellooo", ["hello", "hi", "helo"])
