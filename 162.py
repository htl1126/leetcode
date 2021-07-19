# ref: https://discuss.leetcode.com/topic/7600/a-concise-standard-binary
#              -search-solution
# ref: https://discuss.leetcode.com/topic/13942/my-clean-and-readable-python
#              -solution


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l

# alternate solution, pretty similar
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

if __name__ == '__main__':
    sol = Solution()
    print sol.findPeakElement([1, 2, 3, 1])
