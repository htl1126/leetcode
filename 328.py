# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        p, q, o = head, head.next, head.next
        o_tail = ListNode(None)
        while p and q:
            p.next, q, tmp, o_tail.next = q.next, q.next, q.next, q
            o_tail = o_tail.next
            o_tail.next = None
            if not tmp or not tmp.next:
                break
            else:
                q = tmp
            p, q = p.next, q.next
        r = head
        while r.next:
            r = r.next
        r.next = o
        return head

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    #head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)
    head = sol.oddEvenList(head)
    while head:
        print head.val
        head = head.next
