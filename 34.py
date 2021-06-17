# Ref: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14707/9-11-lines-O(log-n)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(n):
            l, r = 0, len(nums)  # notice the r value
            while l < r:
                m = (l + r) // 2
                if nums[m] < n:
                    l = m + 1
                else:
                    r = m
            return l
        left = search(target)
        # case nums = [1, 2, 2, 3], target = 4 will lead to nums[left:left + 1] == []
        return [left, search(target + 1) - 1] if target in nums[left:left + 1] else [-1, -1]

if __name__ == '__main__':
    sol = Solution()
    print sol.searchRange([5, 7, 7, 8, 8, 10], 8)
