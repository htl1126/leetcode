# ref: https://leetcode.com/discuss/33150/python-solution


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy
        while next is not None and next.next is not None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    res = sol.removeElements(head, 6)
    while res:
        print res.val
        res = res.next
