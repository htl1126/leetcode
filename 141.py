# ref: https://leetcode.com/discuss/40120/except-ionally-fast-python


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

if __name__ == '__main__':
    sol = Solution()
    node = ListNode(1)
    print sol.hasCycle(node)
