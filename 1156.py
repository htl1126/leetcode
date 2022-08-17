# Ref: https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        groups = [[c, len(list(g))] for c, g in itertools.groupby(text)]
        count = collections.Counter(text)
        # if text is "aabbccaa", ans is 3 (swap text[2] and text[6])
        # if text is "aabbcc", ans is 2 (no swaps)
        ans = max(min(k + 1, count[c]) for c, k in groups)
        for i in range(1, len(groups) - 1):  # start from the second group
            # case 1: aaa...abaaa...axyza (groups[i - 1][1] + 1 + groups[i + 1][1])
            #                i          j, swap indexes i and j
            # case 2: aaa...abaaa...a (count[groups[i + 1][0]])
            #                i      j, swap indexes i and j
            if groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:
                ans = max(ans, min(groups[i - 1][1] + 1 + groups[i + 1][1], count[groups[i + 1][0]]))
        return ans
