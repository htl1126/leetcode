# Ref: https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/discuss/355386/JavaPython-3-Sliding-Window-O(n)-code-w-brief-explanation-and-analysis.

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        zeros = min_swap = window_size - sum(data[:window_size])
        for i in range(window_size, len(data)):
            if data[i - window_size] == 0:
                zeros -= 1
            if data[i] == 0:
                zeros += 1
            min_swap = min(min_swap, zeros)
        return min_swap
