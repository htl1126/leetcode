# Ref: https://leetcode.com/problems/add-bold-tag-in-string/discuss/104263/Java-solution-Same-as-Merge-Interval.

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        interval = []
        for w in dict:
            i, size = 0, len(w)
            i = s.find(w, i)
            while i != -1:
                interval.append([i, i + size - 1])
                i = s.find(w, i + 1)
        
        interval.sort()
        merged = []
        for i, j in interval:
            if not merged or i > merged[-1][1] + 1:
                merged.append([i, j])
            else:
                merged[-1][1] = max(merged[-1][1], j)
        
        if not merged:
            return s
        ans = ""
        for i, (x, y) in enumerate(merged):
            if i == 0:
                ans += s[0:x] + "<b>" + s[x:y + 1] + "</b>"
            else:
                ans += s[merged[i - 1][1] + 1:merged[i][0]] + "<b>" + s[x:y + 1] + "</b>"
        ans += s[merged[-1][1] + 1:]
        return ans
