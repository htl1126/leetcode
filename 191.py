class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))
