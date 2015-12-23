# faster solution
# source: https://leetcode.com/discuss/54724/python-140ms-beats-100%25-and-works-for-n-sum-n-2

import sys
from leetcode_util import read_list

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in xrange(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]]
                                 , results)
        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

if __name__ == '__main__':
    sol = Solution()
    print sol.fourSum(read_list(sys.argv[1]), int(sys.argv[2]))
