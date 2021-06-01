# Ref: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/683267/Python-O(1)-using-two-hash-tables-beats-97-explained

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.idx = [], {}
        self.num_elem = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx:
            return False
        self.vals.append(val)
        self.idx[val] = self.num_elem
        self.num_elem += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.idx:
            if self.idx[val] != self.num_elem - 1:
                insert_val = self.vals[-1]
                idx = self.idx[val]
                self.vals[idx], self.idx[insert_val] = insert_val, idx
            self.num_elem -= 1
            self.vals.pop()  # pop at the end is O(1)
            self.idx.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
