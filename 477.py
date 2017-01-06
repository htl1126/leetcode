# ref: https://discuss.leetcode.com/topic/72149/python-via-strings


class Solution(object):
    def totalHammingDistance(self, nums):
        """ 
        :type nums: List[int]
        :rtype: int
        """
        return sum(b.count('0') * b.count('1') for b in zip(*(map('{:032b}'.format, nums))))

if __name__ == '__main__':
    sol = Solution()
    print sol.totalHammingDistance([4, 14, 2])
