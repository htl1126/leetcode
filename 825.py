# Ref: https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127029/C%2B%2BJavaPython-Easy-and-Straight-Forward

import collections

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
        c = collections.Counter(ages)
        ans = 0
        for a in c:
            for b in c:
                if request(a, b):
                    if a != b:
                        ans += c[a] * c[b]
                    else:
                        ans += c[a] * (c[a] - 1)
        return ans
        
if __name__ == "__main__":
    sol = Solution()
    print sol.numFriendRequests([16, 17, 18])
