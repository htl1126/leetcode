# Ref: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/446376/JavaC%2B%2BPython-Binary-Search
# Algo: binary search

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) / 2
            if sum((n + mid - 1) / mid for n in nums) > threshold:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    sol = Solution()
    print sol.smallestDivisor([1, 2, 5, 9], 6)
