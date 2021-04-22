# Ref: https://leetcode.com/problems/custom-sort-string/discuss/116615/JavaPython-3-one-Java-10-liner-Python-6-liner-and-2-liner-solutions-w-comment

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ans, cnt = [], collections.Counter(T)
        for c in S:
            if c in cnt:
                ans.append(c * cnt.pop(c))
        for c, v in cnt.items():
            ans.append(c * v)
        return ''.join(ans)
