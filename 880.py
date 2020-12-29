# Ref: https://leetcode.com/problems/decoded-string-at-index/discuss/156747/C%2B%2BPython-O(N)-Time-O(1)-Space

class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if N >= K:
                break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0:
                    return c
                N -= 1

if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeAtIndex("ha22", 5))