import heapq


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, [2, 3, 5]))
        while len(uglies) < n:
            ugly = merged.next()
            if ugly != uglies[-1]:
                uglies += ugly,
        return uglies[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.nthUglyNumber(6)
