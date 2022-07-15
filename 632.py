# Ref: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        q = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(q)

        right = max(nums[i][0] for i in range(len(nums)))
        ans = [float('-inf'), float('inf')]
        # In each iteration, we pick one number from each array and get the range.
        # When any number reaches the end in its array, we should stop because we can't
        # have a smaller range anymore.
        while q:
            left, i, j = heapq.heappop(q)
            if right - left < ans[1] - ans[0]:
                ans = [left, right]
            if j == len(nums[i]) - 1:
                return ans
            v = nums[i][j + 1]
            right = max(right, v)
            heapq.heappush(q, (v, i, j + 1))
