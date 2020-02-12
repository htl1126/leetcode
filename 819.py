# Ref: https://leetcode.com/problems/most-common-word/discuss/123854/C%2B%2BJavaPython-Easy-Solution-with-Explanation
import collections
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        words = re.findall(r"\w+", paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

if __name__ == "__main__":
    sol = Solution()
    print sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
