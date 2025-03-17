class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []

        while i < len(nums1) and j < len(nums2):
            i_1, val_1 = nums1[i]
            i_2, val_2 = nums2[j]

            if i_1 < i_2:
                ans.append([i_1, val_1])
                i += 1
            elif i_2 < i_1:
                ans.append([i_2, val_2])
                j += 1
            else:
                ans.append([i_1, val_1 + val_2])
                i += 1
                j += 1

        while i < len(nums1):
            ans.append(nums1[i])
            i += 1

        while j < len(nums2):
            ans.append(nums2[j])
            j += 1

        return ans

