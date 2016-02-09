import sys
from leetcode_util import read_list

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        print nums, k
        dic = {}
        for i in xrange(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = (i, i, 999999)
            else:
                temp = dic[nums[i]]
                if i - temp[1] < temp[2]:
                    dic[nums[i]] = (temp[1], i, i - temp[1])
        for val in dic.values():
            if val[2] <= k:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.containsNearbyDuplicate(read_list(sys.argv[1]), sys.argv[2])
