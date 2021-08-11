class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        level, depth = [root], 0
        while level:
            new = []
            for node in level:
                for child in node.children:
                    new.append(child)
            level = new
            depth += 1
        return depth
