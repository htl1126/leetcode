import sys

# binary search

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin, end = 0, len(nums) - 1
        middle = (begin + end) / 2
        if target < nums[begin]:
            return 0
        if target > nums[end]:
            return end + 1
        while True:
            if begin + 1 == end:
                if target == nums[begin]:
                    return begin
                elif target == nums[end]:
                    return end
                else:
                    return end
            if target > nums[middle]:
                begin = middle  
                middle = (begin + end) / 2
            elif target < nums[middle]:
                end = middle
                middle = (begin + end) / 2
            else:
                return middle

if __name__ == '__main__':
    sol = Solution()
    nums = [int(num) for num in sys.argv[1].split(',')]
    target = int(sys.argv[2])
    print sol.searchInsert(nums, target)
