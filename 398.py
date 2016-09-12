# ref: https://discuss.leetcode.com/topic/58365/python-zero-liner
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.pick = lambda target: random.choice(
            [i for i, num in enumerate(nums) if num == target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
