class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.ans = 0
        self.get_sum(nestedList, 1)
        return self.ans

    def get_sum(self, nestedList, depth):
        for item in nestedList:
            if item.isInteger():
                self.ans += depth * item.getInteger()
            else:
                self.get_sum(item.getList(), depth + 1)

if __name__ == '__main__':
    sol = Solution()
    print sol.depthSum([1, [4, [6]]])
