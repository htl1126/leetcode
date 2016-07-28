class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        bitmap = [0 for _ in xrange(size)]
        res = []

        def get_subset(pos):
            if pos == size:
                res.append([nums[i] for i in xrange(size) if bitmap[i] == 1])
            else:
                for i in xrange(2):
                    bitmap[pos] = i
                    get_subset(pos + 1)
        get_subset(0)
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.subsets([1, 2, 3])
