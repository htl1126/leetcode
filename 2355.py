# Ref: https://leetcode.com/problems/maximum-number-of-books-you-can-take/discuss/2367084/Python3-Increasing-stack-only-record-%22sudden-changes%22.

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        ans = 0
        stack = []
        # sample input: [8,5,2,7,9]
        for i in range(len(books)):
            # we want keep the "key locations" in a monotonic stack to compute the answer
            while stack and books[stack[-1][0]] + (i - stack[-1][0]) >= books[i]:
                stack.pop()
            last_idx, last_sum = stack[-1] if stack else [-1,0]
            # when i == 2, last_idx == -1 (stack == [])
            # so cur_num_shelf should be books[2] since we can't take more than 2 shelves 
            cur_num_shelf = min(i - last_idx, books[i])
            # cur is the maximum number of books we can take up to shelf i
            cur_min, cur_max = books[i], books[i] - (cur_num_shelf - 1)
            cur = last_sum + (cur_min + cur_max) * cur_num_shelf // 2
            stack.append([i, cur])
            ans = max(ans, cur)
        return ans
