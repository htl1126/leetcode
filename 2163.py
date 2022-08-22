# Ref: https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/discuss/1747029/Python-Explanation-with-pictures-Priority-Queue.

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        pre_min, cur_min = [sum(nums[:n])], sum(nums[:n])
        h = [-n for n in nums[:n]]
        heapq.heapify(h)
        for i in range(n, 2 * n):
            cur_pop = -heapq.heappop(h)
            cur_min -= cur_pop
            cur_min += min(cur_pop, nums[i])
            pre_min.append(cur_min)
            heapq.heappush(h, -min(cur_pop, nums[i]))

        suf_max, cur_max = [sum(nums[2 * n:])], sum(nums[2 * n:])
        h = [n for n in nums[2 * n:]]
        heapq.heapify(h)
        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heapq.heappop(h)
            cur_max -= cur_pop
            cur_max += max(cur_pop, nums[i])
            suf_max.append(cur_max)
            heapq.heappush(h, max(cur_pop, nums[i]))
        suf_max = suf_max[::-1]

        ans = float('inf')
        for a, b in zip(pre_min, suf_max):
            ans = min(ans, a - b)
        return ans
