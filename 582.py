# Ref: https://leetcode.com/problems/kill-process/discuss/103170/Simple-Python-BFS-Solution
# Algo: BFS

import collections
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        tree = collections.defaultdict(list)
        for i in xrange(len(pid)):
            tree[ppid[i]].append(pid[i])
        ans = [kill]
        for i in ans:
            ans.extend(tree.get(i, []))
        return ans


if __name__ == "__main__":
    sol = Solution()
    print sol.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)
