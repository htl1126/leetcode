# ref: https://leetcode.com/articles/wiggle-subsequence/ (see the graph of #5)
# ref: https://discuss.leetcode.com/topic/51807/3-lines-o-n-python-with
#              -explanation-proof
# After removing adjecent duplicate numbers, we can ensure every extreme numbers
# together form a longest wiggle sequence
import itertools


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        norep = [num for num, _ in itertools.groupby(nums)]
        triples = zip(norep, norep[1:], norep[2:])
        return sum((b > a) == (b > c) for a, b, c in triples) + len(norep[:2])

if __name__ == '__main__':
    sol = Solution()
    print sol.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8])
