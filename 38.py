class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            cur, temp, count = s[0], "", 0
            for c in s:
                if cur == c:
                    count += 1
                else:
                    temp += str(count) + cur
                    cur = c
                    count = 1
            temp += str(count) + cur
            s = temp
        return s

if __name__ == '__main__':
    sol = Solution()
    print sol.countAndSay(6)
