# Ref: https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
        	pigs += 1
        return pigs

if __name__ == '__main__':
	sol = Solution()
	print sol.poorPigs(25, 15, 60)
