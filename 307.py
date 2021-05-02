# ref: https://discuss.leetcode.com/topic/33747/148ms-python-solution-binary
#              -indexed-tree
# ref: http://blog.csdn.net/l664675249/article/details/50157669
# ref: http://codeforces.com/blog/entry/18051
# ref: https://cp-algorithms.com/data_structures/segment_tree.html


class NumArray:

    def __init__(self, nums: List[int]):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index: int, val: int) -> None:
        n = self.l + index
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    def sumRange(self, left: int, right: int) -> int:
        m = self.l + left
        n = self.l + right
        ans = 0
        while m <= n:
            if m & 1 != 0:
                ans += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                ans += self.tree[n]
                n -= 1
            n >>= 1
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == '__main__':
    numArray = NumArray([1, 3, 5])
    print numArray.sumRange(0, 2)
    numArray.update(1, 2)
    print numArray.sumRange(0, 2)
