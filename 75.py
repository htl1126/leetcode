# ref: https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, cur, two = 0, 0, len(nums) - 1
        # "zero" is always less than or equal to "cur",
        # and whenever we exchange nums[cur] and nums[two], cur won't change.
        # We don't change "cur" when nums[cur] == 2 and will process it
        # in the next iteration (by checking its value is 0 or 1)
        while cur <= two:
            if nums[cur] == 0:
                nums[zero], nums[cur] = nums[cur], nums[zero]
                zero += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[two] = nums[two], nums[cur]
                two -= 1


if __name__ == '__main__':
    sol = Solution()
    print sol.sortColors(read_list(sys.argv[1]))
