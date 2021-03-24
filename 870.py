# Ref: https://leetcode.com/problems/advantage-shuffle/discuss/149842/Python-Greedy-Solution-Using-Sort

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]
