# Ref: https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/502589/Python-O(n)-sol-by-pre-order-traversal.-75%2B-With-explanation

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def get_nodes(node):
            node_list = []
            if node:
                node_list.append(node.val)
                if node.left:
                    node_list += get_nodes(node.left)
                if node.right:
                    node_list += get_nodes(node.right)
            return node_list
        return "#".join(str(val) for val in get_nodes(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        node_list = map(int, data.split('#'))
        def gen_tree(nodes):
            if len(nodes) > 0:
                root = TreeNode(nodes[0])
                i = 1
                while i < len(nodes):
                    if nodes[i] > nodes[0]:
                        break
                    i += 1
                root.left = gen_tree(nodes[1:i])
                root.right = gen_tree(nodes[i:])
                return root
        return gen_tree(node_list)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    codec = Codec()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    s = codec.serialize(root)
    print s
    out = codec.deserialize(codec.serialize(root))
    print out.val, out.left.val, out.left.left.val
