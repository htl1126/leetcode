# ref: https://leetcode.com/discuss/18242/clean-iterative-solution
#              -binary-searches-with-explanation


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        i, j = 0, len(nums) - 1
        while i < j:  # find the left boundary
            mid = (i + j) / 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        left_bound = i if nums[i] == target else -1
        i, j = 0, len(nums) - 1
        while i < j:  # find the right boundary
            mid = (i + j) / 2 + 1  # the tricky part
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        right_bound = i if nums[i] == target else -1
        return [left_bound, right_bound]

if __name__ == '__main__':
    sol = Solution()
    print sol.searchRange([5, 7, 7, 8, 8, 10], 8)
