# Ref: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf')]
        ans = 0
        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                ans += mid * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.mctFromLeafValues([6, 2, 4])
