# Ref: https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(n):
            nums[nums[i] % n] += n  # some elements might be added with n's already
        for i in range(1, n):
            if nums[i] < n:
                return i
        return n

if __name__ == '__main__':
    sol = Solution()
    print sol.firstMissingPositive([-3, 9, 16, 4, 5, 16, -4, 9, 26, 2])
