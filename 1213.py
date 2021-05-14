# Ref: https://leetcode.com/problems/intersection-of-three-sorted-arrays/discuss/400496/Python-3-pointers

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i = j = k = 0
        cur_max, ans = 0, []
        size1, size2, size3 = len(arr1), len(arr2), len(arr3)
        while i < size1 and j < size2 and k < size3:
            if arr1[i] == arr2[j] == arr3[k]:
                ans.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                cur_max = max(arr1[i], arr2[j], arr3[k])
                if arr1[i] < cur_max:
                    i += 1
                if arr2[j] < cur_max:
                    j += 1
                if arr3[k] < cur_max:
                    k += 1
        return ans
