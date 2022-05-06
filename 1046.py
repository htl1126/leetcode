# Ref: https://leetcode.com/problems/last-stone-weight/discuss/294956/JavaC%2B%2BPython-Priority-Queue

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]
