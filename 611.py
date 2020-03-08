# Ref: https://leetcode.com/problems/valid-triangle-number/discuss/199315/Python3-O(n2)-pointer-solution

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, n = 0, len(nums)
        nums.sort()
        for i in xrange(n - 1, -1, -1):
            lo, hi = 0, i - 1
            while lo < hi:
                if nums[lo] + nums[hi] > nums[i]:
                    ans += hi - lo
                    hi -= 1
                else:
                    lo +=1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.triangleNumber([2, 2, 3, 4])
