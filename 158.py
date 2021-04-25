# ref: https://discuss.leetcode.com/topic/8795/my-python-40ms-solution/5

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.c_buf = []
    
    def read(self, buf: List[str], n: int) -> int:
        ans = 0
        while n:
            buf4 = [""] * 4
            l = read4(buf4)
            if l:
                self.c_buf += buf4[:l]
            read_len = min(len(self.c_buf), n)
            for _ in range(read_len):
                buf[ans] = self.c_buf.pop(0)
                ans += 1
                n -= 1
            if read_len < 4:
                break
        return ans