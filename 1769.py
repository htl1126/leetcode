# Ref: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/discuss/1075895/Easy-Python-beats-100-time-and-space

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        right_count, right_cost, left_count, left_cost = 0, 0, 0, 0
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                left_count += 1
            left_cost += left_count
            ans[i] += left_cost
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                right_count += 1
            right_cost += right_count
            ans[i] += right_cost
        return ans
