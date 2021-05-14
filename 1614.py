class Solution:
    def maxDepth(self, s: str) -> int:
        ans, cur = 0, 0
        for c in s:
            if c == "(":
                cur += 1
                ans = max(cur, ans)
            elif c == ")":
                cur -= 1
        return ans
