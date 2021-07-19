import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        suc, pre = collections.defaultdict(set), collections.defaultdict(int)
        for a, b in prerequisites:
            suc[b].add(a)
            pre[a] += 1
        free = set(range(numCourses)) - set(pre)
        length = 0
        while free:
            n = free.pop()
            for b in suc[n]:
                pre[b] -= 1
                if not pre[b]:
                    free.add(b)
            length += 1
        return length == numCourses

if __name__ == '__main__':
    sol = Solution()
    print sol.canFinish(2, [[1, 0]])
