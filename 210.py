# ref: https://discuss.leetcode.com/topic/13991/short-and-simple


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre, suc = collections.defaultdict(int), collections.defaultdict(list)
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
                if not pre[b]:
                    free.add(b)
        return out * (len(out) == numCourses)

if __name__ == '__main__':
    sol = Solution()
    print sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
