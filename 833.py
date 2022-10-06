# Ref: https://leetcode.com/problems/find-and-replace-in-string/discuss/130587/C%2B%2BJavaPython-Replace-S-from-right-to-left

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for i, src, t in sorted(zip(indices, sources, targets), reverse=True):
            s = s[:i] + t + s[i + len(src):] if s[i:i + len(src)] == src else s
        return s
