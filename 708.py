# Ref: https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/discuss/198633/Python-One-Pass-Time-O(N)-Space-O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal, head)
        if not head:
            new_node.next = new_node
            return new_node
        node = head
        while True:
            if node.val > node.next.val and (node.val <= insertVal or insertVal <= node.next.val):
                break
            elif node.val <= insertVal <= node.next.val:
                break
            elif node.next == head:
                break
            node = node.next
        new_node.next = node.next
        node.next = new_node
        return head

if __name__ == "__main__":
    sol = Solution()
    print sol.insert(head, insertVal)
