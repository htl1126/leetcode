# ref: https://discuss.leetcode.com/topic/53706/7-liner-python-48ms
# ref: https://discuss.leetcode.com/topic/5999/bucket-sort-java-solution-with
#              -explanation-o-n-time-and-space
# The maximum won't be less than (maxV - minV) / (n - 1) = maxGap
# And the bucket size is maxGap + 1
# We collect numbers into buckets, and check if a larger gap exists between
# buckets


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        maxV, minV = max(nums), min(nums)
        maxGap = (maxV - minV) / (len(nums) - 1)
        bSize = maxGap + 1
        bucket = [[] for _ in xrange((maxV - minV) / bSize + 1)]
        for num in nums:
            bucket[(num - minV) / bSize].append(num)
        bucket = [b for b in bucket if b]
        for i in xrange(1, len(bucket)):
            maxGap = max(maxGap, min(bucket[i]) - max(bucket[i - 1]))
        return maxGap

if __name__ == '__main__':
    sol = Solution()
    print sol.maximumGap([1, 3, 15, 5, 7, 8, 6, 2])
