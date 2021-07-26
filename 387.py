import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d, ans = collections.defaultdict(list), len(s)
        for i, c in enumerate(s):
            d[c].append(i)
        for c in d:
            if len(d[c]) == 1 and d[c][0] < ans:
                ans = d[c][0]
        return ans if ans < len(s) else -1

if __name__ == '__main__':
    sol = Solution()
    print sol.firstUniqChar('loveleetcode')
