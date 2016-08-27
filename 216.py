class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def get_comb(begin, seq):
            if len(seq) == k and sum(seq) == n:
                res.append(seq)
            elif len(seq) < k:
                for i in xrange(begin, 10):
                    if sum(seq) + i <= n:
                        get_comb(i + 1, seq + [i])
            return
        get_comb(1, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum3(3, 15)
