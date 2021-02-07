class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n, pos = len(s), float('-inf')
        ans = [n] * n
        for i in list(range(n)) + list(range(n)[::-1]):
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], abs(i - pos))
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestToChar("loveleetcode", "e"))
