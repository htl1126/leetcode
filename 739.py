# Ref: https://leetcode.com/problems/daily-temperatures/discuss/136017/Elegant-Python-Solution-with-Stack
# Algo: stack

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
                print i, t
                print ans
            stack.append(i)

        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
