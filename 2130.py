# Ref: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/discuss/1680417/C%2B%2B-Python-mid-and-reverse-solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        ans = 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        while prev:
            ans = max(ans, head.val + prev.val)
            head, prev = head.next, prev.next
            
        return ans
