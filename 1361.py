# ref: https://leetcode.com/problems/validate-binary-tree-nodes/discuss/939381/Python%3A-clean-BFS-96-faster-TimeComplexity%3A-O(n)-Space-Complexity%3A-O(n)

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root, children = 0, set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i
        queue, visited = [root], set()
        for node in queue:
            if node in visited:
                return False
            visited.add(node)
            if leftChild[node] != -1:
                queue.append(leftChild[node])
            if rightChild[node] != -1:
                queue.append(rightChild[node])
        return len(visited) == n
