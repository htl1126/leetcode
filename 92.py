# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(None)
        dummy.next, pre, begin = head, dummy, head
        for _ in xrange(m - 1):
            pre, begin = pre.next, begin.next
        end = begin
        for _ in xrange(n - m):
            end = end.next
        next_end, p, q = end.next, begin, begin.next
        for _ in xrange(n - m):
            q.next, tmp = p, q.next
            p, q = q, tmp
        pre.next, begin.next = end, next_end
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = sol.reverseBetween(head, 1, 5)
    while head:
        print head.val
        head = head.next
