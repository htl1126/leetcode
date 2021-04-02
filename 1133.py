class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        count = collections.Counter(A)
        if any(x for x in count if count[x] == 1):
            return max(x for x in count if count[x] == 1)
        else:
            return -1
