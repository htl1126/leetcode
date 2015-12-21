import sys
import bisect
from leetcode_util import read_list

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num = sorted(nums)
        smallest_sum = sum(num[:3])
        if target < smallest_sum:
            return smallest_sum
        largest_sum = sum(num[-3:])
        if target > largest_sum:
            return largest_sum
        temp_sum = smallest_sum
        best_sum = temp_sum
        
        diff = abs(temp_sum - target)
        
        for i in xrange(len(num) - 2):
            left = bisect.bisect_left(num, target - num[i] - num[-1], lo=i + 1)
            if left > i + 1:
                left -= 1
            for j in xrange(left, len(num) - 1):
                num_to_find = target - num[i] - num[j]
                ind = bisect.bisect_left(num, num_to_find, lo=j + 1)
                
                values = [ind - 1, ind]
                for value in values:
                    if value > j and value < len(num):
                        temp_sum = num[i] + num[j] + num[value]
                        if temp_sum == target:
                            return temp_sum
                        elif abs(temp_sum - target) < diff:
                            diff = abs(temp_sum - target)
                            best_sum = temp_sum
                if num[i] + num[j] + num[j + 1] > target:
                    break
        return best_sum

if __name__ == '__main__':
    sol = Solution()
    print sol.threeSumClosest(read_list(sys.argv[1]), int(sys.argv[2]))
