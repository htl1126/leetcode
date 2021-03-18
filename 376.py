# Ref: https://leetcode.com/problems/wiggle-subsequence/discuss/162996/python-O(n)-time-O(1)-space-easy-to-understand-16-ms-solution-beats-100


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length, up = 1, None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False
        return length

if __name__ == '__main__':
    sol = Solution()
    print sol.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
