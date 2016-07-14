# ref: https://discuss.leetcode.com/topic/49571/9-lines-recursive-
#              without-helper


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return ListNode(1)
        plused = self.plusOne(head.next)
        head.val += plused != head.next
        if head.val <= 9:
            return head
        head.val = 0
        plused.next = head
        return plused

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(9)
    ans = sol.plusOne(head)
    while ans:
        print ans.val
        ans = ans.next
