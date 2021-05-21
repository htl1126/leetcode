# ref: https://discuss.leetcode.com/topic/35762/9-lines-python-10-lines-c


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                t = []
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        for tail in sentences(j):
                            if tail:
                                t.append(s[i:j] + ' ' + tail)
                            else:
                                t.append(s[i:j])
                memo[i] = t
            return memo[i]
        return sentences(0)

if __name__ == '__main__':
    sol = Solution()
    print sol.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"])
