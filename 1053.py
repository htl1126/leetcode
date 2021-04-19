# Ref: https://leetcode.com/problems/previous-permutation-with-one-swap/discuss/516381/PythonJavaC%2B%2B-easy-to-understand-O(n)-solution

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        # good code for checking index value after leaving the loop
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr
        max_i = i + 1
        for j in range(i + 1, len(arr)):
            if arr[max_i] < arr[j] < arr[i]:
                max_i = j
        arr[i], arr[max_i] = arr[max_i], arr[i]
        return arr
