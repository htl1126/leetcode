class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ""
        cset = "abcdefghijklmnopqrstuvwxyz"
        for i in range(n):
            j = min(26, k - (n - i - 1))
            ans += str(cset[j - 1])
            k -= j
        return ans[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.getSmallestString(5, 73))
