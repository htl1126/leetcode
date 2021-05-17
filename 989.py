# Ref: https://leetcode.com/problems/add-to-array-form-of-integer/discuss/234488/JavaC%2B%2BPython-Take-K-itself-as-a-Carry

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        return [int(i) for i in str(k)] + num if k else num
