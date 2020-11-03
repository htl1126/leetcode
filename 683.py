# Ref: https://leetcode.com/problems/k-empty-slots/discuss/107931/JavaC%2B%2B-Simple-O(n)-solution

class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        size = len(bulbs)
        days = [0 for _ in xrange(size)]
        for i in xrange(size):
            days[bulbs[i] - 1] = i + 1
        left, right = 0, K + 1
        i, ans = 0, size + 1
        while right < size:
            if days[i] <= days[left] or days[i] <= days[right]:
                if i == right:
                    ans = min(ans, max(days[left], days[right]))
                left, right = i, i + K + 1
            i += 1
        return -1 if ans == size + 1 else ans

if __name__ == "__main__":
    sol = Solution()
    print sol.kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4], 2)
