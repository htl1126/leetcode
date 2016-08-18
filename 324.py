# ref: https://discuss.leetcode.com/topic/32861/3-lines-python-with-explanation
#              -proof


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

if __name__ == '__main__':
    sol = Solution()
    num = [4, 5, 5, 6]
    sol.wiggleSort(num)
    print num
