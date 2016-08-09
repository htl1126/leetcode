class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = len(nums) + 1
        for i in xrange(1, len(nums)):
            nums[i] += nums[i - 1]
        for i in xrange(len(nums)):
            if i == 0:
                target = s
            else:
                target = nums[i - 1] + s
            begin, left, right = i, i, len(nums) - 1
            while left < right:
                mid = (left + right) / 2
                if nums[mid] >= target:
                    if mid == left or nums[mid - 1] < target:
                        ans = min(ans, mid - begin + 1)
                        break
                    right = mid
                else:
                    left = mid + 1
            if nums[left] >= target:
                ans = min(ans, left - begin + 1)
        return ans if ans <= len(nums) else 0

if __name__ == '__main__':
    sol = Solution()
    print sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
