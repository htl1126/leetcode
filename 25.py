# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or not head:
            return head
        dummy = ListNode(None)
        dummy.next = head
        begin, cur = head, head
        prebegin, postcur = None, cur.next
        cur_len = 1
        while cur:
            if cur_len == k:
                p, q = begin, begin.next
                for i in xrange(k - 1):
                    q.next, tmp = p, q.next
                    if i == 0:
                        p.next = postcur
                        cur = p
                    p, q = q, tmp
                begin = p
                if prebegin:
                    prebegin.next = begin
                else:
                    dummy.next = begin
                prebegin, begin, cur = cur, postcur, postcur
                if not cur:
                    break
                postcur = cur.next
                cur_len = 1
            cur = cur.next
            cur_len += 1
            if postcur:
                postcur = postcur.next
            else:
                break
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    res = sol.reverseKGroup(None, 2)
    while res:
        print res.val
        res = res.next
