# ref: https://discuss.leetcode.com/topic/33747/148ms-python-solution-binary
#              -indexed-tree
# ref: http://blog.csdn.net/l664675249/article/details/50157669


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.size, self.nums = len(nums), nums
        self.tbl = [0] * (self.size + 1)
        for i in xrange(self.size):
            k = i + 1
            while k <= self.size:
                self.tbl[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff, self.nums[i] = val - self.nums[i], val
        i += 1
        while i <= self.size:
            self.tbl[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        ans, j = 0, j + 1
        while j:
            ans += self.tbl[j]
            j -= (j & -j)
        while i:
            ans -= self.tbl[i]
            i -= (i & -i)
        return ans

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)

if __name__ == '__main__':
    numArray = NumArray([1, 3, 5])
    print numArray.sumRange(0, 2)
    numArray.update(1, 2)
    print numArray.sumRange(0, 2)
