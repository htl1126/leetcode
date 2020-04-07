# Ref: https://leetcode.com/problems/next-closest-time/discuss/107776/Python

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        return min((t <= time, t) for i in xrange(24 * 60)
                                  for t in ["%02d:%02d" % divmod(i, 60)]
                                  if set(t) <= set(time))[1]

if __name__ == "__main__":
    sol = Solution()
    print sol.nextClosestTime("19:34")
