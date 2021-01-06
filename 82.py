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
        if not head:
            return None
        prehead = pre = ListNode(next=head)
        while head and head.next:
            if head.next.val == head.val:
                cur = head.next
                while cur and cur.val == head.val:
                    cur = cur.next
                head = pre.next = cur
            else:
                pre, head = head, head.next
        return prehead.next

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
