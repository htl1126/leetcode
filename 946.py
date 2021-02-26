# Ref: https://leetcode.com/problems/validate-stack-sequences/discuss/197685/C%2B%2BJavaPython-Simulation-O(1)-Space

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack, i = [], 0
        for v in pushed:
            stack.append(v)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    print sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
