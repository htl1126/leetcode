# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
        
if __name__ == "__main__":
    sol = Solution()
    print sol.getDecimalValue(head)
