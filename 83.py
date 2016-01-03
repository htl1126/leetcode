# make use of sorted list nodes
# source: https://leetcode.com/discuss/74268/simple-iterative-python-6-lines-60-ms

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
        ptr = head
        while ptr:
            while ptr.next and ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            ptr = ptr.next
        return head

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    #head.next.next.next = ListNode(3)
    ptr = head
    while ptr:
        print ptr.val
        ptr = ptr.next
    sol.deleteDuplicates(head)
    print 'processing...'
    ptr = head
    while ptr:
        print ptr.val
        ptr = ptr.next
