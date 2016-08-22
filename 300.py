# https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-
#         time-with-explanation/2
# The O(nlgn) DP solution
# O(lgn) comes from the trick that the LIS sequence is kept
# And every number in the LIS sequence should be as small as possible
# However the resulting sequence may not be a valid LIS, that is, S[i]
# is the last element of a subsequence of length i


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0 for _ in xrange(len(nums))]
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

if __name__ == '__main__':
    sol = Solution()
    print sol.lengthOfLIS([4, 5, 6, 3])
