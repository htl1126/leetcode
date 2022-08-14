class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        ans, d = [], (100 - discount) / 100
        for w in sentence.split():
            if w[0] == '$' and w[1:].isdecimal():
                ans.append('$' + "%.2f" % (float(w[1:]) * d))
            else:
                ans.append(w)
        return ' '.join(ans)
