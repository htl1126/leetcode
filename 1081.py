# Ref: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/308210/JavaC%2B%2BPython-Stack-Solution-O(N)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            # the while loop here tries to "move" c to a position closer
            # to the stack bottom and popped characters will be added later
            # since they're not the last one in s
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)
