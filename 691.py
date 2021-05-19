# Ref: https://leetcode.com/problems/stickers-to-spell-word/discuss/108333/Rewrite-of-contest-winner's-solution

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = 1 << len(target)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] != float('inf'):
                for sticker in stickers:
                    now = i
                    for s in sticker:
                        for j, c in enumerate(target):
                            if s == c and not ((now >> j) & 1):
                                now |= 1 << j
                                break
                    dp[now] = min(dp[now], dp[i] + 1)
        return dp[-1] if dp[-1] < float('inf') else -1
