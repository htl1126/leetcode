# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        left, right = self.sortList(head), self.sortList(slow)
        pre_head = cur = ListNode(None)
        while left and right:
            if left.val < right.val:
                cur.next, left.next, left = left, None, left.next
            else:
                cur.next, right.next, right = right, None, right.next
            cur = cur.next
        if left or right:
            cur.next = left or right
        return pre_head.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(4)
    head = sol.sortList(head)
    while head:
        print head.val
        head = head.next
