class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            ans = []
            for child in root.children:
                ans += self.postorder(child)
            return ans + [root.val]
        return []
