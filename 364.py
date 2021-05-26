# Ref: https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83641/No-depth-variable-no-multiplication

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        weighted, unweighted = 0, 0
        while nestedList:
            nextLevel = []
            for item in nestedList:
                if item.isInteger():
                    unweighted += item.getInteger()
                else:
                    nextLevel += item.getList()
            weighted += unweighted
            nestedList = nextLevel
        return weighted
