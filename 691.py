# Ref: https://leetcode.com/problems/stickers-to-spell-word/discuss/108318/C%2B%2BJavaPython-DP-%2B-Memoization-with-optimization-29-ms-(C%2B%2B)

class Solution(object):
    def minStickers(self, stickers, target):
        num_sticker = len(stickers)
        s_cnt = [collections.Counter(s) for s in stickers]    
        memo = {}
        memo[""] = 0
        
        def helper(target):
            if target not in memo:
                t_cnt = collections.Counter(target)
                ans = float('inf')
                for i in range(num_sticker):
                    if s_cnt[i][target[0]] == 0:
                        continue
                    s = "".join([c * (n - s_cnt[i][c]) for c, n in t_cnt.items() if n > s_cnt[i][c]])
                    tmp = helper(s)
                    if tmp != -1: 
                        ans = min(ans, 1 + tmp)
                memo[target] = ans if ans < float('inf') else -1
            return memo[target]
        
        return helper("".join(sorted(target)))
