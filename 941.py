class Solution:
    def validMountainArray(self, arr: list) -> bool:
        if len(arr) < 3:
            return False
        size = len(arr)
        i = 0
        while i < size - 1 and arr[i] < arr[i + 1]:
            i += 1
        j = size - 1
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1
        return i != 0 and j != size - 1 and i == j

if __name__ == "__main__":
    sol = Solution()
    print(sol.validMountainArray([3, 5, 5]))
