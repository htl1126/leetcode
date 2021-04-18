import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        ans = Sum = 0
        count[0] = 1  # edge case, used for count[0] + ... + count[i] = K
        for i in xrange(len(nums)):
            Sum += nums[i]
            ans += count[Sum - k]
            count[Sum] += 1  # found another subsequence, so add one
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.subarraySum([1, 1, 1], 2)

# Algorithm: dynamic programming
# Ref: https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation
