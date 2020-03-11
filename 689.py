# Ref: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/203666/python-sliding-windows-O(n)O(1)

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        w1, w2, w3 = sum(nums[:k]), sum(nums[k:2 * k]), sum(nums[2 * k:3 * k])
        max_w1, max_w2, max_w3 = w1, w1 + w2, w1 + w2 + w3
        max_w1_idx, max_w2_idx, max_w3_idx = [0], [0, k], [0, k, 2 * k]
        for i in xrange(1, len(nums) - 3 * k + 1):
            cur_w1 = sum(nums[i:i + k])
            cur_w2 = sum(nums[i + k:i + 2 * k])
            cur_w3 = sum(nums[i + 2 * k:i + 3 * k])
            if cur_w1 > max_w1:
                max_w1, max_w1_idx = cur_w1, [i]
            if cur_w2 + max_w1 > max_w2:
                max_w2, max_w2_idx = cur_w2 + max_w1, max_w1_idx + [i + k]
            if cur_w3 + max_w2 > max_w3:
                max_w3, max_w3_idx = cur_w3 + max_w2, max_w2_idx + [i + 2 * k]
        return max_w3_idx

if __name__ == "__main__":
    sol = Solution()
    print sol.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
