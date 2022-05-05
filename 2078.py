# Ref: https://leetcode.com/problems/two-furthest-houses-with-different-colors/discuss/1589141/JavaC%2B%2BPython-O(n)-Solution

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i, j = 0, len(colors) - 1
        while colors[-1] == colors[i]:
            i += 1
        while colors[0] == colors[j]:
            j -= 1
        return max(len(colors) - i - 1, j)
