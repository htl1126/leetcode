# ref: https://discuss.leetcode.com/topic/62139/python-solution-dp-and-binary
#              -search


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(mid):
            count = 0
            current = 0
            for n in nums:
                current += n
                if current > mid:
                    count += 1
                    if count >= m:
                        return False
                    current = n
            return True

        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l + h ) / 2
            if valid(mid):
                h = mid
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    sol = Solution()
    print sol.splitArray([7, 2, 5, 10, 8], 2)
