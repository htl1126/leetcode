# ref: https://discuss.leetcode.com/topic/34491/clever-idea-making-it-simple


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                num = nums[mid]
            else:
                if target < nums[0]:  # must be '<' not '<='
                    num = - float('inf')
                else:
                    num = float('inf')
            if num < target:
                left = mid + 1
            elif num > target:
                right = mid - 1
            else:
                return mid
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.search([1], 1)
