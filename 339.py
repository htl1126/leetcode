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

# stack version
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        s = [[nestedList, 0, 1]]
        ans = 0
        while s:
            arr, i, d = s[-1]
            if i == len(arr):
                s.pop()
            else:
                s[-1][1] += 1
                if arr[i].isInteger():
                    ans += arr[i].getInteger() * d
                else:
                    s.append([arr[i].getList(), 0, d + 1])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.depthSum([1, [4, [6]]])
