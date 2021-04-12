class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if k > arr[mid] - mid - 1:
                l = mid + 1
            else:
                r = mid
        if k <= arr[l] - l - 1:
            return arr[l] - ((arr[l] - l) - k)
        return arr[l] + (k - (arr[l] - l - 1))
