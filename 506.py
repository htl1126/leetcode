class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score2 = [(i, v) for i, v in enumerate(score)]
        score2.sort(key=lambda x: x[1], reverse=True)
        ans = [""] * len(score)
        for i, pair in enumerate(score2):
            j = pair[0]
            if i == 0:
                ans[j] = "Gold Medal"
            elif i == 1:
                ans[j] = "Silver Medal"
            elif i == 2:
                ans[j] = "Bronze Medal"
            else:
                ans[j] = str(i + 1)
        return ans
