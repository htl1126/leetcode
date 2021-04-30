# ref: https://discuss.leetcode.com/topic/27608/java-python-one-pass-solution-o
#              -n-time-o-n-space-using-buckets


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(d[m - 1] - nums[i]) <= t:
                return True
            if m + 1 in d and abs(d[m + 1] - nums[i]) <= t:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] // w]
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.containsNearbyAlmostDuplicate([-1, -1], 1, 0)
