# ref: https://leetcode.com/discuss/54608/python-concise-solution-with-comments


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        if abs(len(s) - len(t)) > 1 or s == t:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isOneEditDistance('ab', 'ba')
