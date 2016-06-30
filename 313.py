# ref: https://leetcode.com/discuss/72763/python-generators-on-a-heap
import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = merged.next()
            if ugly != uglies[-1]:
                uglies += ugly,
        return uglies[-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.nthSuperUglyNumber(14, [3, 5, 7])
