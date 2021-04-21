# Ref: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        for f in sorted(folder):
            if not ans or not f.startswith(ans[-1] + '/'):
                ans.append(f)
        return ans
