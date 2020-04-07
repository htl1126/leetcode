# Ref: https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity

import collections

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1:
                return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W:
                opened -= start.popleft()
        return opened == 0

if __name__ == "__main__":
    sol = Solution()
    print sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
