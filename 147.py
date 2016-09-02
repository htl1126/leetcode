# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre_head = ListNode(None)
        pre_head.next = head
        sorted_end, cur = head, head.next
        while cur:
            if cur.val >= sorted_end.val:
                sorted_end, cur = sorted_end.next, cur.next
            else:
                pre, ptr = pre_head, pre_head.next
                while cur.val >= ptr.val:
                    pre, ptr = ptr, ptr.next
                sorted_end.next, pre.next, cur.next, cur = (
                    cur.next, cur, ptr, sorted_end.next.next)
        return pre_head.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head = sol.insertionSortList(head)
    while head:
        print head.val
        head = head.next
