# ref: https://leetcode.com/discuss/51759/share-my-dynamic-programming
#              solution-with-explaination


class Solution(object):
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = {0: [[]], 1: [[s[0]]]}
        for i in range(1, len(s)):
            ans[i + 1] = []
            for j in range(i + 1):
                t = s[j:i + 1]
                if t == t[::-1]:
                    for sol in ans[j]:
                        ans[i + 1].append(sol + [t])
        return ans[len(s)]

if __name__ == '__main__':
    sol = Solution()
    print sol.partition('aab')
