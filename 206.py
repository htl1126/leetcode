# source: https://leetcode.com/discuss/84948/clear-iterative-python-solution

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        p, q = head, head.next
        p.next = None

        while q:
            tmp, q.next = q.next, p
            p, q = q, tmp

        return p


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    sol = Solution()
    new_head = sol.reverseList(head)
    print new_head.val
    print new_head.next.val
    print new_head.next.next.val
    print new_head.next.next.next.val
