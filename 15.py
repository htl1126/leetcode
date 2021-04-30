# using list pointers
# fix one element as x, then set y, z to find all solutions for - x = y + z

import sys
from leetcode_util import read_list

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        size = len(nums)
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, size - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSum(read_list(sys.argv[1]))
