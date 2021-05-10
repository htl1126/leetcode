# Ref: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/683267/Python-O(1)-using-two-hash-tables-beats-97-explained

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d_direct = {}
        self.d_invert = {}
        self.num_elem = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d_invert:
            return False
        self.d_direct[self.num_elem] = val
        self.d_invert[val] = self.num_elem
        self.num_elem += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d_invert:
            return False
        ind = self.d_invert.pop(val)
        self.d_direct.pop(ind)
        if ind != self.num_elem - 1:
            self.d_direct[ind] = self.d_direct[self.num_elem - 1]
            self.d_invert[self.d_direct[self.num_elem - 1]] = ind
            self.d_direct.pop(self.num_elem - 1)
        self.num_elem -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.d_direct[random.randint(0, self.num_elem - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
