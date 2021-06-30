# ref: https://discuss.leetcode.com/topic/53896/frugal-python-code
import collections
import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.idxs, self.set_size = [], collections.defaultdict(set), collections.defaultdict(int)
        self.num_elem = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.vals.append(val)
        self.idxs[val].add(self.num_elem)
        self.set_size[val] += 1
        self.num_elem += 1
        return self.set_size[val] == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.idxs[val]:
            idx, last_val = self.idxs[val].pop(), self.vals[-1]
            self.set_size[val] -= 1
            self.vals[idx] = last_val
            self.idxs[last_val].add(idx)
            self.idxs[last_val].discard(self.num_elem - 1)
            self.vals.pop()
            self.num_elem -= 1
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vals)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
