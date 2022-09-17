class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        d = {}
        for w in words:
            d[int(w[-1:])] = w[:-1]
        ans = []
        for i in range(1, 10):
            if i in d:
                ans.append(d[i])
        return " ".join(ans)
