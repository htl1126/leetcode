# Ref: https://leetcode.com/problems/reorganize-string/discuss/113435/4-lines-Python

class Solution:
    def reorganizeString(self, S: str) -> str:
        a = sorted(sorted(S), key=S.count)  # Case "abba" needs double sorted()
        h = len(a) // 2
        a[1::2], a[::2] = a[:h], a[h:]
        return "".join(a) * (a[-2] != a[-1])

if __name__ == "__main__":
    sol = Solution()
    print sol.reorganizeString("aaab")
