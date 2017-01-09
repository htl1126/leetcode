# ref: https://discuss.leetcode.com/topic/71456/short-python
# ref: https://discuss.leetcode.com/topic/71464/10-lines-python-with
#              -easy-understanding


import bisect

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        return max(min(abs(house - heater)
                       for i in [bisect.bisect(heaters, house)]
                       for heater in heaters[i - (i > 0):i + 1])
                   for house in houses)

if __name__ == '__main__':
    sol = Solution()
    print sol.findRadius([1, 2, 3, 4], [1, 4])
