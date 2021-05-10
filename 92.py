# Ref: https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right or not head:
            return head
        dummy = pre_m = ListNode()
        dummy.next = head
        for _ in range(left - 1):
            pre_m = pre_m.next
        tail = pre_m.next
        for _ in range(right - left):
            tmp = pre_m.next
            pre_m.next = tail.next
            tail.next = tail.next.next
            pre_m.next.next = tmp
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
