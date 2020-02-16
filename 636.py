# Ref: https://leetcode.com/problems/exclusive-time-of-functions/discuss/105100/Python-Straightforward-with-Explanation
# Algo: stack

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack, ans = [], [0 for _ in xrange(n)]
        prev_time = 0
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print sol.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
