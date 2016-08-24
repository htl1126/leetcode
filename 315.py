# ref: https://discuss.leetcode.com/topic/31162/mergesort-solution


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                # All the numbers in two halves are sorted. We picked the
                # bigger one in one half and placed it at enum[len(enum) - 1],
                # enum[len(enum) - 2]..., etc. If we picked one from the left,
                # we updated the number by the length of the right, because all
                # the numbers in the right are less than the number picked in
                # the left currently.
                for i in xrange(len(enum) - 1, -1, -1):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

if __name__ == '__main__':
    sol = Solution()
    print sol.countSmaller([5, 2, 6, 1])
