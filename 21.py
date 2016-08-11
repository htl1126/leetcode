# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return l1 or l2
        dummy = node = ListNode(None)
        while l1 or l2:
            if l1 and not l2:
                node.next, l1 = l1, l1.next
            elif l2 and not l1:
                node.next, l2 = l2, l2.next
            else:
                if l1.val < l2.val:
                    node.next, l1 = l1, l1.next
                else:
                    node.next, l2 = l2, l2.next
            node = node.next
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head_1 = ListNode(1)
    head_1.next = ListNode(3)
    head_2 = ListNode(2)
    head_2.next = ListNode(4)
    res = sol.mergeTwoLists(head_1, head_2)
    while res:
        print res.val
        res = res.next
