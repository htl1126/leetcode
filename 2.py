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
        ans = ListNode(0)
        pre = prehead = ListNode(next=ans)
        while l1 or l2:
            if l1:
                ans.val += l1.val
                l1 = l1.next
            if l2:
                ans.val += l2.val
                l2 = l2.next
            if ans.val >= 10:
                ans.val -= 10
                ans.next = ListNode(val=1)
            else:
                ans.next = ListNode(val=0)
            pre, ans = ans, ans.next
        if ans.val == 0:
            pre.next = None
        return prehead.next
