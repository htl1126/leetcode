# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        ans = head = ListNode(None)
        while l1 or l2:
            ans.next = ListNode(0)
            ans = ans.next
            if l1:
                ans.val += l1.val
                l1 = l1.next
            if l2:
                ans.val += l2.val
                l2 = l2.next
            ans.val += carry
            carry = ans.val >= 10
            if carry:
                ans.val -= 10
        if carry:
            ans.next = ListNode(1)
        return head.next
