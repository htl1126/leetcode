class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 1. find root node (left -1 right -1)
        # 2. visit from root with DFS
        # 3. can visit all the nodes (every node should visit only once) with any root => true
        #    else false
        root_cand = set(range(n))
        g = {}
        for i in range(n):
            g[i] = []
            if leftChild[i] != -1:
                g[i].append(leftChild[i])
                if leftChild[i] in root_cand:
                    root_cand.remove(leftChild[i])
            if rightChild[i] != -1:
                g[i].append(rightChild[i])
                if rightChild[i] in root_cand:
                    root_cand.remove(rightChild[i])
        if len(root_cand) != 1:
            return False
        visited = [False] * n
        def dfs(i):
            if visited[i]:
                return False
            visited[i] = True
            if g[i]:
                return all(map(dfs, g[i]))
            return True
        return dfs(root_cand.pop()) and all(visited)
