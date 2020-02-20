# Ref: https://leetcode.com/problems/reorganize-string/discuss/113435/4-lines-Python

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = sorted(sorted(S), key=S.count)
        h = len(a) / 2
        a[1::2], a[::2] = a[:h], a[h:]
        return "".join(a) * (a[-1:] != a[-2:-1])

if __name__ == "__main__":
    sol = Solution()
    print sol.reorganizeString("aaab")
