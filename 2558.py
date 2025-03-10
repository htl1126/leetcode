# ref: https://leetcode.com/problems/take-gifts-from-the-richest-pile/solutions/3144075/python3-heap

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        nums = [-num for num in gifts]
        heapq.heapify(nums)

        for _ in range(k):
            t = math.isqrt(-heapq.heappop(nums))
            heapq.heappush(nums, -t)

        return -sum(nums)

