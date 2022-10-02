# Ref: https://leetcode.com/problems/filling-bookcase-shelves/discuss/323415/simple-Python-DP-solution

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            curr_width, curr_height = shelfWidth, 0
            j = i - 1
            while j >= 0 and curr_width >= books[j][0]:
                curr_width -= books[j][0]
                curr_height = max(curr_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + curr_height)
                j -= 1
        return dp[-1]
