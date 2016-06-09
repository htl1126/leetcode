class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        rot = start
        start, end = 0, len(nums) - 1
        n = len(nums)
        while start <= end:
            mid = (start + end) / 2
            realmid = (mid + rot) % n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print sol.search([1], 1)
