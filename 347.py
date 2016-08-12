# ref: https://discuss.leetcode.com/topic/44323/1-line-python-solution-using-
#              counter-with-explanation
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return zip(*collections.Counter(nums).most_common(k))[0]

if __name__ == '__main__':
    sol = Solution()
    print sol.topKFrequent([1, 1, 2, 2, 2, 3], 2)
