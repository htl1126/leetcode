# Ref: https://leetcode.com/problems/jump-game-vi/discuss/1260843/C%2B%2BJavaPython-DP-and-Decreasing-Deque-Clean-and-Concise-Time-O(N)-Space-O(K)

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = collections.deque([0])
        for i in range(1, n):
            # nums[i] becomes the best score obtained at index i
            nums[i] = nums[dq[0]] + nums[i]
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i - dq[0] >= k:
                dq.popleft()
        return nums[-1]
