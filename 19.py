# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p1 = p2 = pre = dummy
        for _ in xrange(n):
            p1 = p1.next
        while p1:
            p1, p2, pre = p1.next, p2.next, p2
        pre.next = p2.next
        return dummy.next
