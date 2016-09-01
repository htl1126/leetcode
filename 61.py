# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not k or not head:
            return head
        list_len, cur, last = 0, head, None
        while cur:
            last, cur, list_len = cur, cur.next, list_len + 1
        k %= list_len
        if k:
            k = list_len - k
            pre, cur = None, head
            for _ in xrange(k):
                pre, cur = cur, cur.next
            pre.next = None
            last.next, head = head, cur
        return head

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head = sol.rotateRight(head, 6)
    while head:
        print head.val
        head = head.next
