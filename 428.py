# Ref: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/150790/Python-O(n)-recursive-both-functions

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        s = []
        def preorder(node):
            if not node:
                return
            s.append(str(node.val))
            for child in node.children:
                preorder(child)
            s.append('#')
        preorder(root)
        return ' '.join(s)
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        q = collections.deque(data.split())

        def helper():
            if not q:
                return None
            node = Node(int(q.popleft()), [])
            while q[0] != '#':
                node.children.append(helper())
            q.popleft()  # remove the '#'
            return node

        return helper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
