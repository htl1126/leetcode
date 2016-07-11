# ref: https://discuss.leetcode.com/topic/21610/11-lines-o-n-2-python


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        for k in xrange(len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
        return count

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSumSmaller([-2, 0, 1, 3], 2)
