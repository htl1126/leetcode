# finding the second half of the list and reversing it is really tricky
# source: https://leetcode.com/discuss/69366/short-python-solution

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        prev = ListNode('')
        prev.next = head
        curr = head
        fast = head
        while fast and fast.next:
            prev = prev.next
            curr = curr.next
            fast = fast.next.next
        prev.next = None
        new_head = None
        while curr:
            tmp = curr.next
            curr.next = new_head
            new_head = curr
            curr = tmp
        while head and new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True
        
if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    print sol.isPalindrome(head)
