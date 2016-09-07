class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        vals = []

        def get_value(nestedList, depth):
            if len(vals) < depth:
                vals.append([])
            for item in nestedList:
                if item.isInteger():
                    vals[depth - 1].append(item.getInteger())
                else:
                    get_value(item.getList(), depth + 1)
        get_value(nestedList, 1)
        return sum((len(vals) - idx) * sum(vals_item)
                   for idx, vals_item in enumerate(vals))
