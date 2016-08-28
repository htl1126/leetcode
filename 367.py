class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo, hi = 1, num
        while lo < hi:
            mid = (lo + hi) / 2
            curr_sq = mid ** 2
            if curr_sq < num:
                lo = mid + 1
            elif curr_sq > num:
                hi = mid - 1
            else:
                return True
        return lo ** 2 == num

if __name__ == '__main__':
    sol = Solution()
    print sol.isPerfectSquare(101)
