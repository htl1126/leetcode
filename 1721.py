# Ref: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1013859/Python-Solution-with-Explanation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # 10, 7, (10 - 7 + 1) = 4
        fast = head
        for _ in range(k - 1):
            fast = fast.next
        first = fast
        slow = head
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.val, first.val = first.val, slow.val
        return head
