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
            else:
                for i in xrange(begin + 1, 10):
                    if sum(seq) + i <= n:
                        get_comb(i, seq + [i])
                    else:
                        return
        get_comb(0, [])
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum3(3, 15)
