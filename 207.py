import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        suc, pre = collections.defaultdict(set), collections.defaultdict(set)
        for a, b in prerequisites:
            suc[b].add(a)
            pre[a].add(b)
        free = set(range(numCourses)) - set(pre)
        length = 0
        while free:
            n = free.pop()
            for b in suc[n]:
                pre[b].discard(n)
                if not pre[b]:
                    free.add(b)
            length += 1
        return length == numCourses

if __name__ == '__main__':
    sol = Solution()
    print sol.canFinish(2, [[1, 0]])
