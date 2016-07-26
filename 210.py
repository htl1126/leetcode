# ref: https://discuss.leetcode.com/topic/13991/short-and-simple


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import *
        pre, suc = defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            pre[a] += 1
            suc[b].append(a)
        free = set(range(numCourses)) - set(pre)
        out = []
        while free:
            a = free.pop()
            out.append(a)
            for b in suc[a]:
                pre[b] -= 1
                pre[b] or free.add(b)
        return out * (len(out) == numCourses)

if __name__ == '__main__':
    sol = Solution()
    print sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
