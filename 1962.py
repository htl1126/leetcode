# Ref: https://leetcode.com/problems/remove-stones-to-minimize-the-total/discuss/1390254/JavaC%2B%2BPython-Heap-Solution-O(klogn)

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-n for n in piles]
        heapq.heapify(piles)
        for i in range(k):
            n = heapq.heappop(piles)
            heapq.heappush(piles, n // 2)
        return -sum(piles)
