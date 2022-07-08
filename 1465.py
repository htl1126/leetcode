# Ref: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/661995/Do-you-like-visual-explanation-You-got-it.-%3A-)-With-2-code-variations.

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def get_cuts(size, cuts, res):
            res.append(cuts[0])
            for i in range(1, len(cuts)):
                res.append(cuts[i] - cuts[i - 1])
            res.append(size - cuts[-1])
        h_list, w_list = [], []
        get_cuts(h, sorted(horizontalCuts), h_list)
        get_cuts(w, sorted(verticalCuts), w_list)
        return max(h_list) * max(w_list) % (10 ** 9 + 7)
