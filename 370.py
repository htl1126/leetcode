# ref: https://discuss.leetcode.com/topic/49691/java-o-k-n-time
#              -complexity-solution/2


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0 for _ in xrange(length)]
        for update in updates:
            ans[update[0]] += update[2]
            if update[1] + 1 < length:
                ans[update[1] + 1] -= update[2]
        for i in xrange(1, length):
            ans[i] += ans[i - 1]
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.getModifiedArray(5, [[1,  3,  2], [2,  4,  3], [0,  2, -2]])
