# Ref: https://leetcode.com/problems/duplicate-zeros/discuss/312727/C%2B%2BJava-Two-Pointers-Space-O(1)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zero_count = sum(arr[i] == 0 for i in range(len(arr)))
        i, j = len(arr) - 1, len(arr) + zero_count - 1
        while i < j:  # when i == j, there's no zero behind arr[i]
            if arr[i] != 0:
                if j < len(arr):
                    arr[j] = arr[i]
            else:
                if j < len(arr):
                    arr[j] = arr[i]
                j -= 1
                if j < len(arr):
                    arr[j] = arr[i]
            i, j = i - 1, j - 1
