class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for i, v in enumerate(nums):
            if v:
                self.dic[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, v in self.dic.items():
            if i in vec.dic:
                ans += v * vec.dic[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

