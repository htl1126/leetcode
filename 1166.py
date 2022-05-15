class TrieNode:
    def __init__(self, val=-1):
        self.children = {}
        self.val = val

class FileSystem:

    def __init__(self):
        self.fs = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        d, items = self.fs, path[1:].split('/')
        if len(items) == 0:
            return False
        for i, s in enumerate(items):
            if s not in d.children:
                if i != len(items) - 1:
                    return False
                d.children[s] = TrieNode()
            d = d.children[s]
        if d.val == -1:
            d.val = value
            return True
        return False

    def get(self, path: str) -> int:
        d, items = self.fs, path[1:].split('/')
        if len(items) == 0:
            return -1
        for i, s in enumerate(items):
            if s not in d.children:
                return -1
            d = d.children[s]
        return d.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
