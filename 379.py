# ref: https://discuss.leetcode.com/topic/53109/4-line-python-solution-using
#              -only-1-set-and-no-queue


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.directory = set(range(maxNumbers))

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return  - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self.directory.pop() if self.directory else -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.directory

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.directory.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

if __name__ == '__main__':
    obj = PhoneDirectory(3)
    print obj.get()
    print obj.get()
