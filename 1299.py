class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max, new_max = -1, -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(cur_max, arr[i])
            arr[i] = cur_max
            cur_max = new_max
        return arr
