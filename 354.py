# ref: https://discuss.leetcode.com/topic/48160/python-o-nlogn-o-n-solution
#              -beats-97-with-explanation


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def liss(envs):
            def limp(envs, tails, k):
                begin, end = 0, len(tails) - 1
                while begin <= end:
                    mid = (begin + end) >> 1
                    if envs[tails[mid]][1] >= k[1]:
                        end = mid - 1
                    else:
                        begin = mid + 1
                return begin
            tails = []
            for i, env in enumerate(envs):
                idx = limp(envs, tails, env)
                if idx >= len(tails):
                    tails.append(i)
                else:
                    tails[idx] = i
            return len(tails)

        def f(x, y):
            return -1 if (x[0] < y[0] or x[0] == y[0] and x[1] > y[1]) else 1
        envelopes.sort(cmp=f)
        return liss(envelopes)

if __name__ == '__main__':
    sol = Solution()
    print sol.maxEnvelopes([[2, 3], [5, 4], [6, 7], [6, 4]])
