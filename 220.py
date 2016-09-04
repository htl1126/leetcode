# ref: https://discuss.leetcode.com/topic/27608/java-python-one-pass-solution-o
#              -n-time-o-n-space-using-buckets


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        d = {}
        w = t + 1
        for i in xrange(len(nums)):
            b = nums[i] / w
            if b in d:
                return True
            if b + 1 in d and abs(d[b + 1] - nums[i]) < w:
                return True
            if b - 1 in d and abs(d[b - 1] - nums[i]) < w:
                return True
            d[b] = nums[i]
            if i >= k:
                del d[nums[i - k] / w]
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.containsNearbyAlmostDuplicate([-1, -1], 1, 0)
