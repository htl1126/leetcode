# ref: https://discuss.leetcode.com/topic/31011/python-same-solution-as-142
#              -linked-list-cycle-ii
# consider nums[a] = b as a -> b, find where the cycle starts


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while slow != finder:
                    slow = nums[slow]
                    finder = nums[finder]
                return finder

if __name__ == '__main__':
    sol = Solution()
    print sol.findDuplicate([3, 4, 1, 2, 5, 1])
