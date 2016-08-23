# ref: https://discuss.leetcode.com/topic/33770/short-simple-o-n-log-n


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        first = [0]
        for num in nums:
            first.append(first[-1] + num)

        def sort(lo, hi):
            mid = (lo + hi) / 2
            if mid == lo:  # We just return 0 for length 1 subsequence
                return 0
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in first[lo:mid]:  # two while loops work because of the
                while i < hi and first[i] - left < lower: i += 1  # sorted subsequence
                while j < hi and first[j] - left <= upper: j += 1
                count += j - i  # add the number of right values
            first[lo:hi] = sorted(first[lo:hi])
            return count
        return sort(0, len(first))

if __name__ == '__main__':
    sol = Solution()
    print sol.countRangeSum([-2, 5, -1], -2, 2)
