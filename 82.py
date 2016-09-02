# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre_begin = ListNode(None)
        pre_head = pre_begin
        pre_begin.next, begin, pre_cur, cur = head, head, head, head.next
        while cur:
            if begin.val != cur.val:
                if begin != pre_cur:
                    pre_begin.next, begin, pre_cur, cur = (
                        cur, cur, cur, cur.next)
                else:
                    pre_begin, begin, pre_cur, cur = (
                        pre_begin.next, begin.next, pre_cur.next, cur.next)
            else:
                pre_cur, cur = pre_cur.next, cur.next
        # deal with the last streak
        if begin.val == pre_cur.val and begin != pre_cur:
            pre_begin.next = None
        return pre_head.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(2)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(3)
    head = sol.deleteDuplicates(head)
    while head:
        print head.val
        head = head.next
