# Ref: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/discuss/1623436/JavaPython-3-From-O(n-*-logn)-to-average-O(n)-w-brief-explanation-and-analysis.

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        h = []
        for i, n in enumerate(nums):
            heapq.heappush(h, (n, i))
            if len(h) > k:
                heapq.heappop(h)
        return [a[0] for a in sorted(h, key=lambda x: x[1])]
