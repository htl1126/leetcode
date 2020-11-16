# Ref: https://leetcode.com/problems/remove-interval/discuss/441085/1-liner

class Solution(object):
    def removeInterval(self, intervals, (A, B)):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for a, b in intervals:
            if a < A:
                res.append([a, min(b, A)])
            if b > B:
                res.append([max(a, B), b])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.removeInterval([[0, 2], [3, 4], [5, 7]], [1, 6])
