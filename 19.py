# Ref: similar to https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1013859/Python3Visualization-Two-Pointers-Solution-with-Explanation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre, first, second = None, head, head
        for _ in range(n - 1):
            second = second.next
        while second.next:
            pre, first, second = first, first.next, second.next
        if pre:
            pre.next = first.next
        else:
            head = first.next
        return head
